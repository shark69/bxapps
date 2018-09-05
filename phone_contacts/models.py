from django.db import models
from core.models import TimeStampedModel

# Create your models here.

class Contact(TimeStampedModel):

# user_id INT
# first_name varchar(45)
# last_name varchar(45)

	contact_id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=45)
	last_name = models.CharField(max_length=45)

	def __str__(self):
		return self.first_name

class Email(TimeStampedModel):

# email_id int
# email varchar(45)

	email_id = models.AutoField(primary_key=True)
	email_description = models.CharField(max_length=45)

class Email_type(TimeStampedModel):

# email_type_id int
# email_type varchar(45)

	email_type_id = models.AutoField(primary_key=True)
	email_type = models.CharField(max_length=45)

class Phone(TimeStampedModel):

# phone_id int
# phone_number int

	phone_id = models.AutoField(primary_key=True)
	phone_number = models.CharField(max_length=45)

class Phone_type(TimeStampedModel):

# phone_type_id int
# phone_type varchar (20)

	phone_type_id = models.AutoField(primary_key=True)
	phone_type = models.CharField(max_length=45)

class Contact_has_email(TimeStampedModel):

# user_id int
# email_id int
# email_type_id int

	contact = models.OneToOneField(Contact, on_delete=models.CASCADE, primary_key=True,)
	email = models.ForeignKey(Email, on_delete=models.CASCADE)
	email_type = models.ForeignKey(Email_type, on_delete=models.CASCADE)

class Contact_has_phone(TimeStampedModel):

# user_id int
# phone_id int
# phone_type_id

	contact = models.OneToOneField(Contact, on_delete=models.CASCADE, primary_key=True,)
	phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
	phone_type = models.ForeignKey(Phone_type, on_delete=models.CASCADE)