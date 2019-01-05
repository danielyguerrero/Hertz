# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..login.models import User
from django.db import models

# Create your models here.

class ReservationManager(models.Manager):
	
	def validate(self, form_data, user_id):
		user = User.objects.get(id=user_id)
		errors = []
		pu_location = form_data['pu_location']
		do_location = form_data['do_location']
		vehicle = form_data['vehicle']

		if len(form_data['first_name']) == 0:
			errors.append("First name is required.")

		if len(form_data['last_name']) == 0:
			errors.append('Last name is required.')

		if len(form_data['email']) == 0:
			errors.apend('Email is required.')

		if len(form_data['phone']) == 0:
			errors.append('Phone number is required.')

		return errors	

	def add_res(self, form_data, user_id):
		user = User.objects.get(id=user_id)
		reservation = self.create(
			pu_location = form_data['pu_location'],
			do_location = form_data['do_location'],
			vehicle = form_data['vehicle']

			)





class Reservation(models.Model):
	vehicle = models.CharField(max_length=45)
	pu_location = models.CharField(max_length=45)
	do_location = models.CharField(max_length=45)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = ReservationManager()





