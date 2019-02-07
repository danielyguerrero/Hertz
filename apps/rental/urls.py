from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^$', views.index, name= 'dashboard'),
	url(r'add$',views.add, name='add_res'),
	url(r'locations$',views.locations, name='locations'),
	url(r'requirements$', views.requirements, name='requirements'),
	url(r'^delete/(?P<res_id>[0-9]+)$', views.delete, name="delete"),
	url(r'^logout$',views.logout, name='logout'),

]



