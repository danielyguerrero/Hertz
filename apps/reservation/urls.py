from django.conf.urls import url
from . import views


urlpatterns = [

	url(r'^$', views.index, name= 'dashboard'),
	url(r'add$',views.add_res, name='add_res'),

]



