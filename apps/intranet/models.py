from __future__ import unicode_literals
from django.db import models
import bcrypt

class EmployeeManager(models.Manager):

	def validate_login(self, form_data):
		errors = []

		if len(form_data['user_id']) == 0:
			errors.append('Employee Username is Required.')
		if len(form_data['password']) == 0:
			errors.append('Password is Required.')

		if not errors:
			employee = Employee.objects.filter(user_id=form_data['user_id']).first()
			if employee:
				password = form_data['password'].encode()
				db_password = employee.password.encode()

				if bcrypt.checkpw(password, db_password):
					return {'employee' : employee}

		errors.append('Login failed')
		return	{'errors': errors}



class Employee(models.Model):
	user_id = models.CharField(max_length=45)
	password = models.CharField(max_length=45)

	objects = EmployeeManager()