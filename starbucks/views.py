from django.shortcuts import render, redirect, get_object_or_404
from membership.models import Review
from order.models import Coffee,Desserts,Goods
import random


def give_reviews(request):
    reviews = Review.objects.all().order_by('-id')
    reviews5 = reviews[0:5]

    # 김은수 ------------
    coffee = Coffee.objects.all()
    coffee_list = coffee[0:3]
    desserts = Desserts.objects.all()
    desserts_list = desserts[0:3]
    goods = Goods.objects.all()
    goods_list = goods[0:3]
    #------------------
    return render(request, "index.html",
                  {"reviews": reviews5, "coffee": coffee_list, "desserts": desserts_list, "goods": goods_list})
