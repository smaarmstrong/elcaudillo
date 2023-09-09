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
