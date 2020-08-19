from django.shortcuts import render, redirect, get_object_or_404
from order.models import Coffee, Desserts, Goods, Carts
from accounts.models import User
from django.core.paginator import Paginator
import math


# Create your views here.

# menu 함수 작성 김은수
def menu(request):
    if request.method == "POST":
        redirect("menu.html")
    else:
        coffee = Coffee.objects.all()
        desserts = Desserts.objects.all()
        goods = Goods.objects.all()

        context = {"coffee": coffee, "desserts": desserts, "goods": goods
                   }
        return render(request, 'menu.html', context)

#상세보기 함수 김은수
def detail(request, product_cd):
    if request.method == "POST":
        category = request.GET['kind'].capitalize()
        user = request.session['user_n']
        print(user)
        product = get_object_or_404(category, cd=product_cd)

        cart = Carts()

        return redirect("order:cart")
    else:

        if request.GET['kind'] == 'desserts':

            product = get_object_or_404(Desserts, cd=product_cd)

            category = "desserts"

        elif request.GET['kind'] == 'coffee':

            product = get_object_or_404(Coffee, cd=product_cd)

            category = "coffee"
        else:

            product = get_object_or_404(Goods, cd=product_cd)

            category = "goods"

        context = {"list": product, "category": category }
        return render(request, 'menu_detail.html', context)

#장바구니 함수 김은수
def cart(request):
    if request.method == "POST":
        redirect("cart.html")

    else:
        return render(request, 'cart.html')

# def paging(request, list):
#     paginator = Paginator(list, 3)
#     page = request.GET.get('page')
#     contacts = paginator.get_page(page)
#
#     return contacts
