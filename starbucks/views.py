from django.shortcuts import render, redirect, get_object_or_404
from membership.models import Review

def give_reviews(request) :
    reviews = Review.objects.all().order_by('-id')
    reviews5 = reviews[0:5]

    #김은수


    return render(request, "index.html",{"reviews": reviews5})
