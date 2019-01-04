from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^$', views.index, name= 'dashboard'),
	url(r'reservation/client',views.add_client, name='add_client'),
	url(r'reservation/vehicle',views.vehicle, name='vehicle'),
	url(r'reservation/location',views.location, name='location'),


]



