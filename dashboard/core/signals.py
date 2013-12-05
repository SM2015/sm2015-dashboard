# coding: utf-8
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User

from core.models import DashboardUser

@receiver(post_save, sender=User)
def post_add_user(sender, created, instance, **kw):
    if not created:
        try:
            DashboardUser.objects.get(user=instance)
        except DashboardUser.DoesNotExist:
            dashboard_user = DashboardUser(user=instance)
            dashboard_user.save()

            dashboard_user._send_register_confirmation_email()
