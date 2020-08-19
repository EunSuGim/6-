from django.shortcuts import render, redirect, get_object_or_404
from order.models import Coffee, Desserts, Goods
from django.core.paginator import Paginator
import math


# Create your views here.

# menu 함수 작성 김은수
def menu(request):
    if request == "POST":
        redirect("menu.html")
    else:
        coffee = Coffee.objects.all()
        desserts = Desserts.objects.all()
        goods = Goods.objects.all()

        context = {"coffee": coffee, "desserts": desserts, "goods": goods
                   }
        return render(request, 'menu.html', context)


def detail(request, product_cd):
    if request == "POST":
        redirect("menu_detail.html")
    else:
        if request.GET['kind'] == 'desserts':

            product = get_object_or_404(Desserts, cd=product_cd)

            product_name = "desserts"

        elif request.GET['kind'] == 'coffee':

            product = get_object_or_404(Coffee, cd=product_cd)

            product_name = "coffee"
        else:

            product = get_object_or_404(Goods, cd=product_cd)

            product_name = "goods"

        context = {"list": product, "product_name": product_name}
        return render(request, 'menu_detail.html', context)


def cart(request):
    if request == "POST":
        redirect("cart.html")

    else:
        return render(request, 'cart.html')

# def paging(request, list):
#     paginator = Paginator(list, 3)
#     page = request.GET.get('page')
#     contacts = paginator.get_page(page)
#
#     return contacts
