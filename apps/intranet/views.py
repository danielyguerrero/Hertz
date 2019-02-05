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

	return render(request, 'intranet/index.html')

