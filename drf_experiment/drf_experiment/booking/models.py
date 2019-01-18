# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Booking(models.Model):

    code = models.CharField(unique=True, max_length=6)
