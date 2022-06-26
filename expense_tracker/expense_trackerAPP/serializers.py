from dataclasses import field
from email.policy import default
from .models import *
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciedUser
        fields = ("username","password")
    def save(self):
        password = self.validated_data['password']
        instance = ciedUser(
            username = self.validated_data['username'],
        )
        if password is not None:
            instance.set_password(password)
        instance.save()
        
        
        return instance


class Custom_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")

class Currency_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ("__all__")

class Expense_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Daily_expense
        fields = ("__all__")
        # extra_kwargs = {
        #     'date': {'read_only': True}
        # }

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',"category_name",'totalexpenses')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciedUser
        fields = ('id',"username",'user_expense')


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ('id',"currency_name","currency_value",'currency_expense')

    