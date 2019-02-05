from __future__ import unicode_literals
from django.db import models
import bcrypt




class Employee(models.Model):
	first_name = models.CharField(max)