from dataclasses import field
from .models import *
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ciedUser
        fields = ("name","email","password")
    def save(self):
        password = self.validated_data['password']
        instance = ciedUser(
            name = self.validated_data['name'],
            email = self.validated_data['email']
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