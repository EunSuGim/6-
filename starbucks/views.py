from django.shortcuts import render, redirect, get_object_or_404
from membership.models import Review, History
from accounts.models import User
def give_reviews(request) :
    reviews = Review.objects.all().order_by('-id')
    my_list2 = []
    my_list5 = []
    j=0
    for review in reviews :
        user = get_object_or_404(User, id = review.user_id)
        history = get_object_or_404(History, id = review.history_id)
        temp= (review, user, history)
        my_list5.append(temp)
        if j < 2:
            my_list2.append(temp)

        if j == 4:
            break
        j+=1
    return render(request, "index.html", {"my_list2": my_list2, "my_list5": my_list5})

# def give_footer(request) :
#     reviews = Review.objects.all().order_by('-id')
#     my_list2 = []
#     j=0
#     for review in reviews :
#         user = get_object_or_404(User, id = review.user_id)
#         history = get_object_or_404(History, id = review.history_id)
#         temp= (review, user, history)
#         my_list2.append(temp)
#         j += 1
#         if j == 2:
#             break
#     return render(request, "index.html", {"my_list2": my_list2})