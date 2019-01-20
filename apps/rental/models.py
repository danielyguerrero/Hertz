from __future__ import unicode_literals
from ..login.models import User
from django.db import models

class ReservationManager(models.Manager):
	def validate(self, form_data):
		errors = []
		vehicle = form_data['vehicle']

		pu_location = form_data['pu_location']
		pu_time = form_data['pu_time']
		do_location = form_data['do_location']
		do_time = form_data['do_time']

		if len(form_data['vehicle']) == 0:
			errors.apend('vehicle is required.')
		if len(form_data['pu_location']) == 0:
			errors.append("Pick Up Location is required.")
		if len(form_data['do_location']) == 0:
			errors.append('Drop Off is required.')
		return errors	

	def add_res(self, form_data, user_id):
		if form_data['vehicle'] == "Compact":
			rate = 15.00
		if form_data['vehicle'] == "MidSizeSedan":
			rate = 20.00
		if form_data['vehicle'] == "FullSizeSedan":
			rate = 25.00
		if form_data['vehicle'] == "MidSizeSuv":
			rate = 30.00
		if form_data['vehicle'] == "LargeSuv":
			rate = 40.00
		if form_data['vehicle'] == "Van":
			rate = 50.00
		if form_data['vehicle'] == "PassangerVan":
			rate = 55.00
		if form_data['vehicle'] == "PickupTruck":
			rate = 60.00
		user = User.objects.get(id=user_id)
		reservation = self.create(
		vehicle = form_data['vehicle'],
		pu_location = form_data['pu_location'],
		pu_date = form_data['pu_date'],
		pu_time = form_data['pu_time'],
		do_location = form_data['do_location'],
		do_date = form_data['do_date'],
		do_time = form_data['do_time'],
		rate = rate,
		made_by = user
		)
		print rate
		return reservation

class Reservation(models.Model):
	vehicle = models.CharField(max_length=45)
	pu_location = models.CharField(max_length=45)
	pu_date = models.DateField(null=True)
	pu_time = models.TimeField(null=True)
	do_location = models.CharField(max_length=45)
	do_date = models.DateField(null=True)
	do_time = models.TimeField(null=True)
	rate = models.IntegerField(default=0)
	made_by = models.ForeignKey(User, related_name="made_by")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ReservationManager()

	def __unicode__(self):
		return "id: {}, pu_location: {}, do_location: {}, added_by: {}".format(self.id, self.pu_location, self.do_location, self.added_by)





