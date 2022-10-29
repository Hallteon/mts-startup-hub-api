from django.db import models


class Event(models.Model):
    name = models.TextField(verbose_name='Название')
    platform = models.ForeignKey('Platform', on_delete=models.CASCADE, verbose_name='Платформа')
    description = models.TextField(verbose_name='Описание')
    add_information = models.TextField(blank=True, verbose_name='Дополнительное описание')
    goals = models.TextField(verbose_name='Цели')
    equipment = models.TextField(verbose_name='Оборудование')
    theme = models.TextField(verbose_name='Тема')
    date = models.TextField(verbose_name='Дата')
    time = models.TextField(verbose_name='Время')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Platform(models.Model):
    city = models.TextField(verbose_name='Город')

    class Meta:
        verbose_name = 'Платформа'
        verbose_name_plural = 'Платформы'