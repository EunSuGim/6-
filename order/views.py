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


# 상세보기 함수 김은수
def detail(request, product_cd):
    if request.method == "POST":
        category = request.GET['kind']
        user_id = request.session['user_id']
        quantity = int(request.POST["quantity"])
        session = get_object_or_404(User, user_id=user_id)

        if category == "coffee":
            product = get_object_or_404(Coffee, cd=product_cd)
        elif category == "desserts":
            product = get_object_or_404(Desserts, cd=product_cd)
        else:
            product = get_object_or_404(Goods, cd=product_cd)

        cart = Carts(identity=session)

        all_cart = Carts.objects.filter(identity=session)

        if all_cart.exists():
            for i in all_cart:
                if i.cd == product_cd:
                    i.quantity += quantity
                    i.total = i.price * i.quantity
                    i.save()

                else:
                    cart.name = product.name
                    cart.price = product.price
                    cart.quantity = quantity
                    cart.total = product.price * quantity
                    cart.cd = product_cd
                    cart.category = category

                    cart.save()
                    break

        else:
            cart.name = product.name
            cart.price = product.price
            cart.quantity = quantity
            cart.total = product.price * quantity
            cart.cd = product_cd
            cart.category = category

            cart.save()

        flag = request.POST["flag"]

        if flag == "true":
            return redirect("order:cart")
        else:
            return redirect("/order/{}/detail?kind={}".format(cart.cd, cart.category))
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

        context = {"list": product, "category": category}
        return render(request, 'menu_detail.html', context)


# 장바구니 함수 김은수
def cart(request):
    user_id = request.session['user_id']
    user = get_object_or_404(User, user_id=user_id)
    my_cart = Carts.objects.filter(identity=user)

    total = 0

    for i in my_cart:
        total = total + i.total

    if request.method == "POST":

        pay = request.POST["flag"]

        if pay == "true":
            user.point = user.point - total
            user.save()
            my_cart.delete()
            return redirect("home")
        else:
            return redirect("order:cart")


    else:

        context = {"carts": my_cart, "total": total, "user": user}

        return render(request, 'cart.html', context)


def cart_delete(reqeust, cart_id):
    cart = get_object_or_404(Carts, id=cart_id)
    cart.delete()
    return redirect('order:cart')

# def paging(request, list):
#     paginator = Paginator(list, 3)
#     page = request.GET.get('page')
#     contacts = paginator.get_page(page)
#
#     return contacts
