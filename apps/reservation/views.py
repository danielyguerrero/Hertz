# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from .models import Reservation 



# ==============================================================
# 						RENDER
# ==============================================================

def index(request):
	return render(request, 'reservation/index.html')


def vehicle(request):
	return render(request, 'reservation/vehicle')


# =================================================
#                       PROCESS
# =================================================

def show_trip(request, trip_id):
	trip = Trip.objects.get(id = trip_id)
	context = {
		'users': trip.joined_by.all(),
		'trip': trip
	}
	return render(request, 'travelplanner/trip.html', context)


def add_client(request):
	if request.method == "POST":
		errors = Trip.objects.validate(request.POST)

		if not errors:
			trip = Trip.objects.add_trip(request.POST, request.session["user_id"])
			trip.joined_by.add(current_user(request))
			print trip
			return redirect(reverse('dashboard'))

		flash_errors(request, errors)
		return redirect(reverse('add_trip'))
	else:
		return render(request, 'travelplanner/add.html')



