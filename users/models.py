from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username
    

class Person(models.Model):
    MALE = 1
    FEMALE = 2

    GENDER_FIELD = (
        (MALE, "Male"),
        (FEMALE, "Female")
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    gender = models.PositiveSmallIntegerField(blank=True, null=True, choices=GENDER_FIELD)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField()

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'

    def __str__(self):
        return self.user.username    