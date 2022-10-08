from django.db import models


class Startup(models.Model):
    name = models.CharField(max_length=500, verbose_name='Название')
    application_program = models.ForeignKey('ApplicationProgram', on_delete=models.CASCADE, verbose_name='Программа')
    website = models.CharField(max_length=600, verbose_name='Сайт стартапа')
    stage = models.ForeignKey('Stage', on_delete=models.CASCADE, verbose_name='Стадия разработки')
    description = models.TextField(verbose_name='Описание стартапа')

    class Meta:
        verbose_name = 'Стартап'
        verbose_name_plural = 'Стартапы'


class ApplicationProgram(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Название программы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программа'
        verbose_name_plural = 'Программы'


class Stage(models.Model):
    name = models.CharField(max_length=200, unique=True, verbose_name='Стадия разработки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Стадия разработки'
        verbose_name_plural = 'Стадии разработки'
