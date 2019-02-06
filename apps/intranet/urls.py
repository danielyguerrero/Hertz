from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="intranet"),
    url(r'^Home$', views.emp_login, name='e_login'),
    url(r'^Admin$', views.admin_login, name='a_login'),
]

