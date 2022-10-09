from django.db import models
from django_currentuser.middleware import get_current_user

from users.models import CustomUser


class Startup(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    name = models.TextField(verbose_name='Название')
    program = models.ForeignKey('Program', on_delete=models.CASCADE, verbose_name='Программа')
    website = models.TextField(verbose_name='Сайт стартапа')
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE, verbose_name='Стадия разработки')
    description = models.TextField(verbose_name='Описание стартапа')
    presentation = models.TextField(verbose_name='Презентация')

    def save(self, *args, **kwargs):
        self.user = get_current_user()
        super(Startup, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Стартап'
        verbose_name_plural = 'Стартапы'


class Program(models.Model):
    name = models.TextField(unique=True, verbose_name='Название программы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'


class Stage(models.Model):
    name = models.TextField(unique=True, verbose_name='Стадия разработки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стадия разработки'
        verbose_name_plural = 'Стадии разработки'
