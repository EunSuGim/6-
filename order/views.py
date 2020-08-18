from django.shortcuts import render, redirect, get_object_or_404
from order.models import Coffee, Desserts, Goods


# Create your views here.

# menu 함수 작성 김은수
def menu(request):
    if request == "POST":
        redirect("menu.html")
    else:
        coffee = Coffee.objects.all()
        desserts = Desserts.objects.all()
        goods = Goods.objects.all()
        context = {"coffee": coffee, "desserts": desserts, "goods": goods}
        return render(request, 'menu.html', context)


def c_detail(request, product_cd):
    if request == "POST":
        redirect("menu_detail.html")
    else:
        coffee = get_object_or_404(Coffee, cd=product_cd)

        product = "coffee"

        context = {"list": coffee, "product": product}
        return render(request, 'menu_detail.html', context)


def d_detail(request, product_cd):
    if request == "POST":
        redirect("menu_detail.html")
    else:
        desserts = get_object_or_404(Desserts, cd=product_cd)

        product = "desserts"

        context = {"list": desserts, "product": product}

        return render(request, 'menu_detail.html', context)


def g_detail(request, product_cd):
    if request == "POST":
        redirect("menu_detail.html")
    else:
        goods = get_object_or_404(Goods, cd=product_cd)

        product = "goods"

        context = {"list": goods, "product": product}
        return render(request, 'menu_detail.html', context)


def cart(request):
    if request == "POST":
        redirect("cart.html")

    else:
        return render(request, 'cart.html')
