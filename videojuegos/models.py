# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models 

class Genero(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

class Clasificacion(models.Model):
	titulo = models.CharField(max_length=50)
	nombre = models.CharField(max_length=50)
	descripcion = models.TextField()

	def __str__(self):
	    return self.titulo

class Juego(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=144)
	imagen = models.ImageField(null=True, blank=True, upload_to = "static/img")
	genero = models.ForeignKey(Genero, null=True, blank=True, on_delete=models.CASCADE)
	clasificacion = models.ForeignKey(Clasificacion, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
	    return self.nombre
