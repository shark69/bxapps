# from django.shortcuts import render
from django.shortcuts import render
from .models import Contact

def phone_contacts_list(request):
	contacts = Contact.objects.all()
	return render(request, 'phone_contacts/phone_contacts_list.html', {'contacts':contacts})