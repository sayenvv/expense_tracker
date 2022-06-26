
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import exceptions
import jwt,datetime

# Create your views here.
@api_view(["POST"])
def register(request):
    userserilaizer = RegisterSerializer(data=request.data)
    if userserilaizer.is_valid(raise_exception=True):
        userserilaizer.save()
    data = {'data' : userserilaizer.data}
    return Response(data)

import json
@api_view(["POST"])
def Login(request):
    email = request.data['email']
    password = request.data['password']
    log_cred = ciedUser.objects.filter(email=email).first()
    if log_cred is None:
        raise exceptions.AuthenticationFailed('User Not Found')
    if not log_cred.check_password(password):
        raise exceptions.AuthenticationFailed("password is incorrect")
    payload = {
            'id': log_cred.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1),
            'iat': datetime.datetime.utcnow()
        }
    token = jwt.encode(payload, 'secret', algorithm='HS256')
    response = Response()

    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {
        'jwt': token
    }
    return response

  
@api_view(["GET"])
def userview(request):
    token = request.COOKIES.get('jwt')
    if not token:
        raise exceptions.AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed('Unauthenticated!')

    user = ciedUser.objects.filter(id=payload['id']).first()
    serializer = RegisterSerializer(user)
    return Response(serializer.data)

@api_view(["POST"])
def LogoutView(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response

# Currency
@api_view(["POST"])
def Add_currency(request):
    serializer = Currency_Serializer(data=request.data)
    if(serializer.is_valid()):
        serializer.save()
        data = {'message':"currency added successfully"}
        return Response(data)
    raise exceptions.ValidationError("Not Valid")

# custom categories

@api_view(["POST"])
def Add_customcategories(request):
    serializer = Custom_categorySerializer(data = request.data)
    if(serializer.is_valid()):
        serializer.save()
        data = {'message' : "Category added successfully"}
        return Response(data)
    raise exceptions.ValidationError("unsuccessful")

@api_view(["POST"])
def Add_dailyExpense(request):
    serializer = Expense_Serializer(data=request.data)
    print(serializer)
    if(serializer.is_valid()):
        serializer.save()
        data = {'message' : " added successfully"}
        return Response(data)
    data = {}
    raise exceptions.ValidationError("unsuccessful")

