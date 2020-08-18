from django.shortcuts import render, redirect, get_object_or_404
from order.models import Coffee,Desserts, Goods

# Create your views here.

# menu 함수 작성 김은수
def menu(request): 
    if request == "POST":
        redirect("menu.html")
    else:
        coffee = Coffee.objects.all()
        desserts = Desserts.objects.all()
        goods = Goods.objects.all()
        context = {"coffee" : coffee, "desserts" : desserts, "goods" : goods}
        return render(request, 'menu.html',context)


