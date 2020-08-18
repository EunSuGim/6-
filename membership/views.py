from django.shortcuts import render
from membership.models import Gift_card

def information(request) :
    return render(request,"information.html",{"information":[]})


def history(request) :
    return render(request, "history.html",{"history":[]})


def recharge(request) :
    return render(request, "recharge.html",{"mileage":[]})
     # redirect로 바꿔야함