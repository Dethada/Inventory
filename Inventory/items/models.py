# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.db import models

# Create your models here.
class Items(models.Model):
	title = models.CharField(max_length=100)
	quantity = models.PositiveSmallIntegerField(default=1)
	unit = models.CharField(max_length=50, default='units')
	category = models.CharField(max_length=100, default='Others')
	created_at = models.DateField(default=timezone.now(), blank=True)
	expires_at = models.DateField(null=True, blank=True)
	
	def __str__(self):
		return self.title