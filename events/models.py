from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE, verbose_name='Платформа')
    description = models.CharField(max_length=3000, verbose_name='Описание')
    goals = models.CharField(max_length=500, verbose_name='Цели')
    equipment = models.CharField(max_length=250, verbose_name='Оборудование')
    date = models.CharField(max_length=60, verbose_name='Дата')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Platform(models.Model):
    city = models.CharField(max_length=50, verbose_name='Город')

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'
