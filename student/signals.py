
from django.db.models.signals import pre_save
from django.dispatch import receiver

from student.models import Student


@receiver(pre_save,sender=Student)
def uppercase_username(sender,instance,**kwargs):
    instance.name=instance.name.upper()

