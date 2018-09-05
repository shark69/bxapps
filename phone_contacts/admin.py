from django.contrib import admin
from .models import Contact, Email, Phone


admin.site.register(Contact)
admin.site.register(Email)
admin.site.register(Phone)