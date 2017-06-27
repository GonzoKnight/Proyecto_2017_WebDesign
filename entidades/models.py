# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

# Create your models here.
class tipousuario(models.Model):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre

class usuario(models.Model):
	nombre = models.CharField(max_length=50)
	tipousuario = models.ForeignKey(tipousuario, null=True, blank=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre