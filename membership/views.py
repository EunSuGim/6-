from django.shortcuts import render, get_object_or_404
from membership.models import Gift_card
from accounts.models import User

def information(request,user_n) :
    user = get_object_or_404(User, id=user_n)
    context ={"user" : user}
    return render(request,"information.html",context)


def history(request) :
    return render(request, "history.html",{"history":[]})


def recharge(request) :
    return render(request, "recharge.html",{"mileage":[]})
     # redirect로 바꿔야함