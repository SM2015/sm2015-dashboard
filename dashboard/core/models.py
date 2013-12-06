# coding: utf-8
import random
import hashlib
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
        hash_obj = hashlib.new('md5')
        hash_obj.update(str(random.random())+str(self.user.id))
        key = hash_obj.hexdigest()
        return key
        
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
            
            body_html = u"Dear %s,<br /><br />" % self.user.first_name
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

    def save(self, *args, **kw):
        if not self.id:
            self.activation_key = self._generate_activation_key()
        super(DashboardUser, self).save(*args, **kw)

    def __unicode__(self):
        return self.user.first_name

class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u"Contry"
        verbose_name_plural = "Contries"

class Avance_fisico_y_financiero(models.Model):
    country = models.ForeignKey(Country)

    fecha_de_actualizacion = models.CharField(max_length=100, null=True, blank=True, default=None)
    avance_fisico_planificado = models.CharField(max_length=100, null=True, blank=True, default=None)
    avance_financiero_planificado = models.CharField(max_length=100, null=True, blank=True, default=None)
    avance_fisico_real = models.CharField(max_length=100, null=True, blank=True, default=None)
    avance_financiero_actual = models.CharField(max_length=100, null=True, blank=True, default=None)
    avances_fisicos_original_programado = models.CharField(max_length=100, null=True, blank=True, default=None)
    avances_financieros_original_programado = models.CharField(max_length=100, null=True, blank=True, default=None)
    monto_comprometido = models.CharField(max_length=100, null=True, blank=True, default=None)
    monto_desembolsado = models.CharField(max_length=100, null=True, blank=True, default=None)
    alerta = models.CharField(max_length=100, null=True, blank=True, default=None)
    recomendacion = models.CharField(max_length=100, null=True, blank=True, default=None)

class Hito(models.Model):
    country = models.ForeignKey(Country)

    indicador_de_pago = models.CharField(max_length=100, null=True, blank=True, default=None)
    hito = models.CharField(max_length=100, null=True, blank=True, default=None)
    trimestre = models.CharField(max_length=100, null=True, blank=True, default=None)
    audiencia = models.CharField(max_length=100, null=True, blank=True, default=None)
    estado_actual = models.CharField(max_length=100, null=True, blank=True, default=None)
    alerta_notas = models.CharField(max_length=100, null=True, blank=True, default=None)
    recomendacion = models.CharField(max_length=100, null=True, blank=True, default=None)
    acuerdo = models.CharField(max_length=100, null=True, blank=True, default=None)
    actividad_en_pod = models.CharField(max_length=100, null=True, blank=True, default=None)
