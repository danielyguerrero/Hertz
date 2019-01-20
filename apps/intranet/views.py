from __future__ import unicode_literals
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from ..login.models import User
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

	if user_id not in request.session:
		return	redirect('/')

	user = current_user(request)

	context = {
		'user':user,

	}

	return render(request, 'intranet/index.html', context)

