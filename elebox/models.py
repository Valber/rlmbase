# -*- coding: utf-8 -*-
# Authors Khoteev Sergey
# License GPLv2
from django.db import models
from django.contrib import admin

# Create your models here.

DEVICE_TYPES = (
    (u'devc', u'Device'),
    (u'cond', u'Condensator'),
    (u'ress', u'Resistor'),
    (u'disp', u'Display'),
    (u'conn', u'Connectors'),
    (u'avrm', u'AVR microcontrollers'),
    (u'misc', u'Miscellaneous'),
)


class Corpus(models.Model):
    name = models.CharField(max_length=80)
    draft = models.ImageField(upload_to='pics/corps', blank=True)

    # wrmlfile=models.FileField(upload_to='models') #обязательный
    # параметр, думаю что приложение для локального использования
    # должно уже поставляться с фотками и файлами корпусов.. надо
    # сделать что ли фирменный стиль.... точнее придумать.

    def __unicode__(self):
        return self.name


class CorpusAdmin(admin.ModelAdmin):
    list_display = ('name', )


class Placekeep(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=80)
    pics = models.ImageField(upload_to='pics/place', blank=True)
    place = models.ForeignKey(
        to='Placekeep',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='child_set',
    )

    def __unicode__(self):
        return self.name


class PlacekeepAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class Radioelem(models.Model):
    name = models.CharField(max_length=80)
    typedev = models.CharField(max_length=5,
                               default='misc',
                               choices=DEVICE_TYPES)
    datasheet = models.URLField(blank="TRUE")  # Ссылка на скачивание даташита
    number = models.IntegerField()
    # maxnumber = models.IntegerField() #Это поле должно вычисляться
    manufacturer = models.CharField(max_length=80, blank=True)
    country = models.CharField(max_length=80, default='china')
    place = models.ManyToManyField(Placekeep)
    corpus = models.ForeignKey(to='Corpus', on_delete=models.CASCADE)
    analog = models.ManyToManyField(to='Radioelem',
                                    verbose_name="List Analog",
                                    blank=True)  # список аналогов

    def __unicode__(self):
        return '%s' % (self.name) + " | " + '%s' % (self.corpus)


class RadioelemAdmin(admin.ModelAdmin):
    list_display = ('name', 'typedev', 'number', 'corpus', 'manufacturer',
                    'country')


class Device(models.Model):
    name = models.CharField(max_length=80)
    draft = models.ImageField(upload_to='pics/devfoto', blank=True)
    typedev = models.CharField(max_length=80)
    datasheet = models.URLField(blank="TRUE")  # Ссылка на скачивание даташита
    number = models.IntegerField()
    place = models.ManyToManyField(Placekeep)
    # список деталей которые можно позаимствовать.
    bom = models.TextField(blank=True)

    # bom=models.ManyToManyField("self", verbose_name="List Analog", blank=True)
    def __unicode__(self):
        return '%s' % (self.name) + " | " + '%s' % (self.typedev)

    def get_text_as_list(self):
        text = self.bom
        text_as_list = []  # преобразуем textв список
        A = text.split("\n")
        for i in A:
            text_as_list.append(i.split(";")[:-1])
        return text_as_list


class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'typedev', 'number')


admin.site.register(Device, DeviceAdmin)
admin.site.register(Radioelem, RadioelemAdmin)
admin.site.register(Corpus, CorpusAdmin)
admin.site.register(Placekeep, PlacekeepAdmin)
