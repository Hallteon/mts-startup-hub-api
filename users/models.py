from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email, firstname, lastname, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')

        email = self.normalize_email(email)
        user = self.model(email=email, firstname=firstname, lastname=lastname, **extra_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, firstname, lastname, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, firstname, lastname, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(max_length=80, unique=True, verbose_name='Email')
    firstname = models.TextField(verbose_name='Имя')
    lastname = models.TextField(verbose_name='Фамилия')
    password = models.TextField(verbose_name='Пароль')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']
    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

