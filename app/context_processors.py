# context_processors.py
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from app.models import UserDetail
from app.models import ProductDetail
from app.models import CartDetail


def cart_item_count(request):
    # Retrieve the count of CartDetail objects
    if request.user.is_authenticated:
       N = request.user
    else:
        N=0
    Cartdetail = CartDetail.objects.filter(Name=N)
    count = Cartdetail.count()
    
    # Return it as a dictionary
    return {'count':count}
