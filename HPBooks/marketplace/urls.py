from django.conf.urls import url

from . import views

urlpatterns =[
	url(r'^$', views.dashboard, name='dashboard'),
	url(r'^listings/', views.listings, name='listings'),
	url(r'^createlisting/', views.createlisting, name='createlisting'),
]