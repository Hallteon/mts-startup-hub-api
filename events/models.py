from django.db import models


class Event(models.Model):
    name = models.TextField(verbose_name='Название')
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE, verbose_name='Платформа')
    description = models.TextField(verbose_name='Описание')
    goals = models.TextField(verbose_name='Цели')
    equipment = models.TextField(verbose_name='Оборудование')
    date = models.TextField(verbose_name='Дата')
    time = models.TextField(default='12:12:12', verbose_name='Время')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Platform(models.Model):
    city = models.TextField(verbose_name='Город')

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'
