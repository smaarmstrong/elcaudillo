from django.db import models

# built-in user model
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):

    # models.ForeignKey: field type to establish a relationship between two models
    # User: the model reference; built-in with Django
    #on_delete=models.SET_NULL: if the user is deleted, set the field to null
    # null=FALSE: null is not allowed in the database
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    # models.CharField: field type from Django ORM to store medium length strings
    # models.ImageField: field type from Django ORM to store image files
    # max_length=200: maximum length of strings set to 200
    # null=True: null is permitted to be stored in the database
    # blank=True: the field is allowed to be empty
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    brand = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    
    # models.DecimalField: field type to store decimal numbers
    # max_digits=7: number of digits allowed
    # decimal_places=2: number of decimal places allowed
    rating = models.DecimalField(max_digits=7, decimal_places=2)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    
    # models.IntegerField: field type to store integers
    # default=0: the default value for this field is 0 if no value is provided
    numReviews = models.IntegerField(null=True, blank=True, default=0)
    countInStock = models.IntegerField(null=True, blank=True, default=0)
    
    # models.DateTimeField: field type to store date and time information
    # auto_now_add=True: set so it reflects time and date of record creation
    createdAt = models.DateTimeField(auto_now_add=True)
    
    # _id: _ is a convention to signify a private field
    # models.AutoField: increments each time a new object is made (primary key)
    # primary_key=True: specifies that this field is the primary key for the model
    # editable=False: field cannot be edited through forms or Django admin interface
    _id = models.AutoField(primary_key=True, editable=False)
