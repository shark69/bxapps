from django.urls import path

from . import views

urlpatterns = [
	path('',views.phone_contacts_list, name='phone_contacts_list'),
]