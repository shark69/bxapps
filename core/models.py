# core/models.py
from django.db import models
#from django.contrib.auth.models import User

class TimeStampedModel(models.Model):
	"""
	An abstract base class model that provides selfupdating
	``created`` ``modified`` fields an last user modified.
	"""
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	#user = models.ForeignKey(User) 
	class Meta:
		abstract = True