from decouple import config
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager, 
    PermissionsMixin)
from django.contrib.auth.models import send_mail
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
 
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email'), max_length=255, unique=True)
    first_name = models.CharField(_('first name'), max_length=40, blank=True)
    last_name = models.CharField(_('last name'), max_length=40, blank=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    date_joined = models.DateField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'.strip()
    
    def get_fist_name(self):
        return self.first_name
    
    def email_user(self, subject, message, from_email=config("DEFAULT_FROM_EMAIL")): 
        send_mail(subject, message, from_email, [self.email])
        
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'user'