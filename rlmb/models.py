# -*- coding: UTF-8 -*-
from django.db import models

# Create your models here.

#Пример словаря для выбора значений
QUALITY_CHOICES = (
	(u'A',u'Added'),
	(u'P',u'Verified'),
	(u'B',u'Best'),
)
DEVICE_TYPES = (
	(u'devc',u'Device'),
	(u'disp',u'Display'),
	(u'conn',u'Connectors'),
	(u'avrm',u'AVR microcontrollers'),
	(u'misc',u'Miscellaneous'),
)


class model3D(models.Model):
	name=models.CharField(max_length=80) #название модели
	#ldim=models. #длинна габариты
	#tdim= #габариты - ширины
	#zdim= #габариты - высота
	#fstdfile= #надо сделать по принципу есть нет
	wrmlfile=models.FileField(upload_to='models') #обязательный параметр
	pics=models.ImageField(upload_to='pics/models') #файл картинки
	#лайки
	levq=models.CharField(max_length=2, default='A', choices=QUALITY_CHOICES)#уровень готовности кортеж [добавлено,проверено(на грубые ошибки),одобрено(распространяеться в библиотеках с помощью sync)]

#class Модели схематики

class Schematic(models.Model):
	name=models.CharField(max_length=50)
	#device=models.ManyToManyField(RealElement)
	typedev=models.CharField(max_length=5, default='misc' , choices=DEVICE_TYPES)
	#tstandard=#Тип стандарта[iso,gost]
	#вот тут надо сделать чтобы папка загрузки зависела от параметра класса typedev +self.typedev
	libfile=models.FileField(upload_to='schem') #собственно файл с именем библиотеки
	pics=models.ImageField(upload_to='pics/schem') #картинка с изображением
	#лайки
	levq=models.CharField(max_length=2, choices=QUALITY_CHOICES)#уровень готовности кортеж [добавлено,проверено(на грубые ошибки),одобрено(распространяеться в библиотеках с помощью sync)]


class Footprint(models.Model):
	name=models.CharField(max_length=60) #Имя 
	#tstandart=#Тип стандарта[iso,gost]
	#тип монтажа? (ну или у нас будет здоровая папка где хрен разберешься без базы)
	modfile=models.FileField(upload_to='footprint') #Файл с описанием зарисовки футпринта
	mdcfile=models.FileField(upload_to='footprint') #Файл с описанием.... слабо понятно
	pics=models.ImageField(upload_to='pics/footprint') #картинка с изображением и размерами
	#лайки
	levq=models.CharField(max_length=2, default='A' , choices=QUALITY_CHOICES)#уровень готовности кортеж [добавлено,проверено(на грубые ошибки),одобрено(распространяеться в библиотеках с помощью sync)]

class RealElement(models.Model):
	name=models.CharField(max_length=150)
	manufacturer=models.CharField(max_length=60)
	typedev=models.CharField(max_length=5, default='misc' , choices=DEVICE_TYPES)
	category=models.CharField(max_length=60) #предположительно определяеться кортежом и влияет на расположение схематики
	corps=models.ManyToManyField(model3D) #Список корпусов для этой модели
	shem=models.ManyToManyField(Schematic) #Список схемотехники варианты стандартов гост и исо
	footprint=models.ManyToManyField(Footprint) #Список возможных
	#simmodel=#Cписок доступных форматов симуляции
	datasheet=models.URLField() #Ссылка на скачивание даташита 
	analog=models.ManyToManyField("self")#список аналогов
