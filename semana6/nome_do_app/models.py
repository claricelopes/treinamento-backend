from django.db import models

class App(models.Model):

    titulo = models.CharField(max_length=120)
    cor = models.CharField(max_length=120) 
