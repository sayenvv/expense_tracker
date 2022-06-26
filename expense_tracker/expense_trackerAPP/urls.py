from django.contrib import admin
from django.urls import path,include
from expense_trackerAPP import views

urlpatterns = [

# authentication jwt

    path('register', views.register,name="register"),
    path('Login', views.Login,name="Login"),
    path('userview', views.userview,name="userview"),
    path('LogoutView', views.LogoutView,name="LogoutView"),

# currency

    path('Add_currency', views.Add_currency,name="Add_currency"),

# category
    
    path('Add_customcategories', views.Add_customcategories,name="Add_customcategories"),
    path('Add_dailyExpense', views.Add_dailyExpense,name="Add_dailyExpense"),
    path('Reports', views.Reports,name="Reports"),
    
    
    


]