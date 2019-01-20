from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User
from .models import Reservation 
import datetime



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
	return render(request, 'rental/index.html')

# ==============================================================
# 						RENDER
# ==============================================================

def index(request):

	print "in the index.html"
	#CHECK IS THERE IS A USER_ID IN SESSION
	if 'user_id' not in request.session:

	# RETURN REDIRECT TO THE INDEX.HTML IF USER_ID NOT IN SESSION
	    return redirect('/')

	#ELSE SET VARIABLE "USER" TO EQUAL CURRENT_USER // FROM CURRENT_USER HELPER METHOD ABOVE
	user = current_user(request)

	today = datetime.datetime.now()


	future_res = Reservation.objects.exclude(pu_date = today).filter(made_by = user)

	#PASS VARIABLES THROUGH CONTEXT
	context = {
		'user': user,
		'today': today,
		'future_res': future_res,
	}
	return render(request, 'rental/index.html', context)

# =================================================
#                       PROCESS
# =================================================
def add_res(request):
	if request.method == "POST":
		errors = Reservation.objects.validate(request.POST)
		user = current_user(request)
		pu_date = datetime.datetime.now()
		pu_time = datetime.datetime.now()
		do_date = datetime.datetime.now()
		do_time = datetime.datetime.now()



		if not errors:
			context = {
			'pu_date': pu_date,
			'pu_time': pu_time,
			'do_date': do_date,
			'do_time': do_time,

			}
			reservation = Reservation.objects.add_res(request.POST, request.session["user_id"])
			return redirect(reverse('dashboard'))

		flash_errors(request, errors)
		return redirect(reverse('add_res'))
	else:
		return render(request, 'rental/add.html')



def delete(request, res_id):

    Reservation.objects.get(id=res_id).delete()

    return redirect('dashboard')
