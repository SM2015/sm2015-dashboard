from django.db import models
from django.contrib.auth.models import User

class DashboardUser(models.Model):
    user = models.OneToOneField(User, verbose_name=u"Dashboard User")
    activation_key = models.CharField(max_length=100)
    forgot_password_token = models.CharField(max_length=100, null=True, blank=True, default=None)
    
    def __unicode__(self):
        return self.user.first_name