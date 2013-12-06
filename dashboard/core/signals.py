# coding: utf-8
import random
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
            random_num = random.randrange(1111,9999,1)

            dashboard_user = DashboardUser(user=instance)
            dashboard_user.save()

            temp_password = 'dashboard-{random_num}'.format(random_num=random_num)
            instance.set_password(temp_password)
            instance.save()

            dashboard_user.send_register_confirmation_email(temp_password=temp_password)
