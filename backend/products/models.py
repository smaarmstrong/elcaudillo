from django.db import models

# built-in user model
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model)

# models.ForeignKey: field type to establish a relationship between two models
# User: the model reference; built-in with Django
#on_delete=models.SET_NULL: if the user is deleted, set the field to null
# null=FALSE: null is not allowed in the database
user = models.ForeignKey(User, on_delete=models.SET_NULL, null=False)

# models.CharField: field type from Django ORM to store medium length strings
# max_length=200: maximum length of strings set to 200
# null=True: null is permitted to be stored in the database
# blank=True: the field is allowed to be empty
name = models.CharField(max_length=200, null=True, blank=True)
brand = models.CharField(max_length=200, null=True, blank=True)
category = models.CharField(max_length=200, null=True, blank=True)
