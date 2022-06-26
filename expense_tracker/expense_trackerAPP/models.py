from unicodedata import category
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import F,Sum

# Create your models here.
class ciedUser(AbstractUser):
    username = models.CharField(max_length=256,unique=True)
    password = models.CharField(max_length=256)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    @property
    def user_expense(self):
        total = Daily_expense.objects.filter(user__id=self.id).aggregate(Sum('expense_amount'))
        if total is not None:
            return total['expense_amount__sum']


class Currency(models.Model):
    currency_name = models.CharField(max_length=100)
    currency_value = models.CharField(max_length=100)

    @property
    def currency_expense(self):
        total = Daily_expense.objects.filter(currency__id=self.id).aggregate(Sum('expense_amount'))
        if total is not None:
            return total['expense_amount__sum']

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    status = models.CharField(max_length=25,choices=(('Active','Active'),('suspended','suspended')),default='Active')

    @property
    def totalexpenses(self):
        total = Daily_expense.objects.filter(expense_type__id=self.id).aggregate(Sum('expense_amount'))
        if total is not None:
            return total['expense_amount__sum']
        

class Daily_expense(models.Model):
    expense_type = models.ForeignKey(Category,related_name="category_expense",on_delete=models.CASCADE)
    description = models.TextField()
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
    user = models.ForeignKey(ciedUser,on_delete=models.CASCADE)
    expense_amount = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
