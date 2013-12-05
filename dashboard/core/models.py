# coding: utf-8
import random
import sha
import logging

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import EmailMultiAlternatives

class DashboardUser(models.Model):
    user = models.OneToOneField(User, verbose_name=u"Dashboard User")
    activation_key = models.CharField(max_length=100)
    forgot_password_token = models.CharField(max_length=100, null=True, blank=True, default=None)
    
    def _generate_activation_key(self):
        salt = sha.new(str(random.random())).hexdigest()[:5]
        return sha.new(salt+str(self.user.id)).hexdigest()
        
    def _send_register_confirmation_email(self):
        try:
            to = self.user.email
            from_email = settings.DEFAULT_FROM_EMAIL
            subject = settings.DEFAULT_EMAIL_REGISTER_SUBJECT
            activation_link = "%s/user/activate/?activation_key=%s" % (settings.BASE_URL, self.activation_key)
            
            body = u"Dear {name},".format(name=self.user.first_name)
            body += u"To confirm your registration visit the link below:"
            body += u"{activation_link}".format(activation_link=activation_link)
            body += u"Graciously,"
            body += u"Dashboard Team."
            
            body_html = u"Dear %s,<br /><br />" % self.user.first_name
            body_html += u"To confirm your registration visit the link below:<br /><br />"
            body_html += u"<a href='{activation_link}'>{activation_link}</a><br /><br />".format(activation_link=activation_link)
            body_html += u"graciously,<br />"
            body_html += u"Dashboard Team."

            msg = EmailMultiAlternatives(subject, body, from_email, [to])
            msg.attach_alternative(body_html, "text/html")
            msg.send()

        except Exception:
            logging.exception("[registration] - Error sending email.")
            return False

    def save(self, *args, **kw):
        if not self.id:
            self.activation_key = self._generate_activation_key()
        super(DashboardUser, self).save(*args, **kw)

    def __unicode__(self):
        return self.user.first_name
