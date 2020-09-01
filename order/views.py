from django.shortcuts import render, redirect, get_object_or_404
from order.models import Coffee, Desserts, Goods, Carts, StarbucksAddress
from accounts.models import User
from membership.models import History, Review
from django.core.paginator import Paginator
from django.http import HttpResponse
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
            count = 0
            for i in all_cart:
                if i.cd == product_cd:
                    i.quantity += quantity
                    i.total = i.price * i.quantity
                    i.save()
                    count = 1
                    break

            if count == 0:
                cart.name = product.name
                cart.price = product.price
                cart.quantity = quantity
                cart.total = product.price * quantity
                cart.cd = product_cd
                cart.category = category

                cart.save()

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

        #------------ 근웅 ------------
        histories = History.objects.filter(completed=True)
        reviews = []
        for history in histories:
            if history.cd == product_cd and history.category == category:
                reviews.append( get_object_or_404(Review, history_id = history.id) )

        context = {"list": product, "category": category, "reviews":reviews}
        #-----------------------------
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
            # ----------박근웅----------
            for i in my_cart:
                History.objects.create(user_id=user.id, name=i.name, quantity=i.quantity, total=i.total, cd=i.cd,
                                       category=i.category)
            # -------------------------
            user.point = user.point - total
            if user.point >= 0 :
                user.save()
                my_cart.delete()
                return redirect("/membership/{}/information/history".format(user.id))
            else :
                return HttpResponse('<script type="text/javascript">alert("충전금액이 모자릅니다");</script>')
        else:
            return redirect("order:cart")


    else:

        context = {"carts": my_cart, "total": total, "user": user}

        return render(request, 'cart.html', context)


def cart_delete(reqeust, cart_id):
    cart = get_object_or_404(Carts, id=cart_id)
    cart.delete()
    return redirect('order:cart')


def address(request):
    if request.method == "POST":
        flag = False
        address_list = StarbucksAddress.objects.all()

        search_adr = request.POST.get("input_search")

        result_list = []

        for i in address_list:
            if search_adr in i.address:
                search = StarbucksAddress()
                search.name = i.name
                search.address = i.address
                result_list.append(search)

        context = {"flag": flag, "adr_list": result_list}
        return render(request, 'address.html', context)

    else:
        flag = True
        context = {"flag": flag}
        return render(request, 'address.html', context)


def insert_adr(request):
    user_id = request.session['user_id']

    session = get_object_or_404(User, user_id=user_id)

    test = request.GET.get('adrValue')

    print(test)

    session.select_adr = test

    print(session.select_adr)

    session.save()

    return HttpResponse('<script type="text/javascript">window.close();opener.location.reload();</script>')

# def paging(request, list):
#     paginator = Paginator(list, 3)
#     page = request.GET.get('page')
#     contacts = paginator.get_page(page)
#
#     return contacts
