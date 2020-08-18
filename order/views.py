from django.shortcuts import render, redirect, get_object_or_404
from order.models import Coffee

# Create your views here.

def menu(request):
    if request == "POST":
        redirect("menu.html")
    else:
        coffee = Coffee.objects.all()
        context = {"coffee" : coffee}
        return render(request, 'menu.html',context)


