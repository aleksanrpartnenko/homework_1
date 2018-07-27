# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class ENTRY (models.Model):
    NAME  = models.CharField(max_length=100)
    PLATE  = models.CharField(max_length=6, unique=True )
