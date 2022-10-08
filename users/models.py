from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, firstname=None, lastname=None):
        user_obj = self.model(
            email=email
        )
        user_obj.set_password(password)
        user_obj.email = email
        user_obj.firstname = firstname
        user_obj.lastname = lastname
        user_obj.save(using=self._db)

        return user_obj

    def create_superuser(self, email, password):
        user = self.create_user(email, password)

        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name='Email')
    firstname = models.CharField(max_length=100, verbose_name='Имя')
    lastname = models.CharField(max_length=100, verbose_name='Фамилия')
    password = models.CharField(max_length=30, verbose_name='Пароль')

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

