"""
Definition of models.
"""

from django.db import models

# Create your models here.
class Vestibular(models.Model):
    nome = models.CharField(max_length=200)
class Candidato(models.Model):
    nome = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)    
class Curso(models.Model):
    nome = models.CharField(max_length=200)
    periodo = models.CharField(max_length=50)
    instituicao = models.CharField(max_length=200)

