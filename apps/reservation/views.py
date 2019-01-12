from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User
from .models import Reservation 



# =================================================
# 						HELPERS
# =================================================
def flash_errors(errors, request):
	for error in errors:
		messages.error(request, error)

def current_user(request):
	return User.objects.get(id=request.session['user_id'])

def user(request, id):
	context={
		'user': current_user(request),
	}
	return render(request, 'reservation/index.html')

# ===================================================
# 						RENDER
# ===================================================

def index(request):
	#CHECK IS THERE IS A USER_ID IN SESSION
	if 'user_id' not in request.session:

	# RETURN REDIRECT TO THE INDEX.HTML IF USER_ID NOT IN SESSION
	    return redirect('/')

	#ELSE SET VARIABLE "USER" TO EQUAL CURRENT_USER // FROM CURRENT_USER HELPER METHOD ABOVE
	user = current_user(request)

	#PASS VARIABLES THROUGH CONTEXT
	context = {
		'user': user,
	}
	return render(request, 'reservation/index.html', context)


def add(request):
	if 'user_id' not in request.session:

	# RETURN REDIRECT TO THE INDEX.HTML IF USER_ID NOT IN SESSION
	    return redirect('/')

	#ELSE SET VARIABLE "USER" TO EQUAL CURRENT_USER // FROM CURRENT_USER HELPER METHOD ABOVE
	user = current_user(request)

	#PASS VARIABLES THROUGH CONTEXT
	context = {
		'user': user,
	}
	return render(request, 'reservation/add.html', context)

# =================================================
#                       PROCESS
# =================================================


def add_res(request):
	if request.method == "POST":
		errors = Reservation.objects.validate(request.POST)

		if not errors:
			reservation = Reservation.objects.add_res(request.POST, request.session["user_id"])
			print trip
			return redirect(reverse('dashboard'))

		flash_errors(request, errors)
		return redirect(reverse('add_res'))
	else:
		return render(request, 'reservation/index.html')







