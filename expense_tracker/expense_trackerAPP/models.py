from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ciedUser(AbstractUser):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256,unique=True)
    password = models.CharField(max_length=256)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Currency(models.Model):
    currency_name = models.CharField(max_length=100)
    currency_value = models.CharField(max_length=100)

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    status = models.CharField(max_length=25,choices=(('Active','Active'),('suspended','suspended')),default='Active')

class Daily_expense(models.Model):
    expense_type = models.ForeignKey(Category,on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
    expense_amount = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
