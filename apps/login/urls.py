from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="landing"),
    url(r'^reserve',views.reserve, name="dashboard"),
    url(r'^register$', views.register, name="register"),
    url(r'^login$', views.login, name="login"),

    url(r'^intranet$',views.intranet, name="intranet"),

    url(r'^logout$', views.logout, name="logout")
]



