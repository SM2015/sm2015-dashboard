# coding: utf-8
import random
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.auth.models import User

from core.models import DashboardUser

@receiver(post_save, sender=DashboardUser)
def post_add_user(sender, created, instance, **kw):
    if created:
        random_num = random.randrange(1111,9999,1)

        temp_password = 'dashboard-{random_num}'.format(random_num=random_num)
        instance.user.set_password(temp_password)
        instance.user.save()

        instance.send_register_confirmation_email(temp_password=temp_password)
