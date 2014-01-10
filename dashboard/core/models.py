# coding: utf-8
import random
import hashlib
import logging

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

class Country(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    latlng = models.CharField(max_length=100, default='')
    
    def __unicode__(self):
        return self.name

class DashboardUser(models.Model):
    user = models.OneToOneField(User, verbose_name=u"Dashboard User")
    activation_key = models.CharField(max_length=100)
    forgot_password_token = models.CharField(max_length=100, null=True, blank=True, default=None)
    countries = models.ManyToManyField(Country)
    
    def _generate_token(self):
        hash_obj = hashlib.new('md5')
        hash_obj.update(str(random.random())+str(self.user.id))
        key = hash_obj.hexdigest()
        return key
        
    def send_forgot_password_email(self):
        self.forgot_password_token = self._generate_token()
        self.save()

        try:
            to = self.user.email
            from_email = settings.DEFAULT_FROM_EMAIL
            subject = settings.DEFAULT_EMAIL_FORGOT_PASSWORD_SUBJECT
            forgot_password_link = "%s/user/reset-password/token/%s/" % (settings.BASE_URL, self.forgot_password_token)
            
            body = u"Dear {name},".format(name=self.user.first_name)
            body += u"To update your password access link below:"
            body += u"{link}".format(link=forgot_password_link)
            body += u"Graciously,"
            body += u"Dashboard Team."
            
            body_html = u"Dear %s,<br /><br />".format(name=self.user.first_name)
            body_html += u"To update your password access link below:<br /><br />"
            body_html += u"<a href='{link}'>{link}</a><br /><br />".format(link=forgot_password_link)
            body_html += u"Graciously,<br />"
            body_html += u"Dashboard Team."

            msg = EmailMultiAlternatives(subject, body, from_email, [to])
            msg.attach_alternative(body_html, "text/html")
            msg.send()
            return True

        except Exception:
            logging.error("[FORGOT PASSWORD] - sending email failure.")
            return False

    def send_register_confirmation_email(self, temp_password):
        try:
            to = self.user.email
            from_email = settings.DEFAULT_FROM_EMAIL
            subject = settings.DEFAULT_EMAIL_REGISTER_SUBJECT
            activation_link = "%s/user/activate/?activation_key=%s" % (settings.BASE_URL, self.activation_key)
            
            body = u"Dear {name},".format(name=self.user.first_name)
            body += u"Here is your information account:"
            body += u"Username: {username}".format(username=self.user.username)
            body += u"Password: {password}".format(password=temp_password)
            body += u"Graciously,"
            body += u"Dashboard Team."
            
            body_html = u"Dear {name},<br /><br />".format(name=self.user.first_name)
            body_html += u"Here is your information account:<br />"
            body_html += u"Username: {username}<br />".format(username=self.user.username)
            body_html += u"Password: {password}<br /><br />".format(password=temp_password)
            body_html += u"graciously,<br />"
            body_html += u"Dashboard Team."

            msg = EmailMultiAlternatives(subject, body, from_email, [to])
            msg.attach_alternative(body_html, "text/html")
            msg.send()

        except Exception:
            logging.exception("[registration] - Error sending email.")
            return False

    def __unicode__(self):
        return self.user.first_name
