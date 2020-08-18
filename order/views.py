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


def c_detail(request, product_cd):
    if request == "POST":
        redirect("menu_detail.html")
    else:
        coffee = get_object_or_404(Coffee, cd= product_cd)

        context = {"coffee" : coffee}
        return render(request, 'menu_detail.html',context)

def d_detail(request, product_cd):
    if request == "POST":
        redirect("menu_detail.html")
    else:

        return render(request, 'menu_detail.html')

def g_detail(request, product_cd):
    if request == "POST":
        redirect("menu_detail.html")
    else:

        return render(request, 'menu_detail.html')
