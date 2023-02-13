from django.db import models
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class UserDetails(models.Model):
    name = models.CharField(max_length=225, db_index=True)
    dob = models.DateField()
    email = models.EmailField(_('email address'), unique=True)
    phonenumber = PhoneNumberField(blank=True)

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'rockykhairnar2099@gmail.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.name
