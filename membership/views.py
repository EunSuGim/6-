from django.shortcuts import render, get_object_or_404, redirect
from membership.models import Gift_card, History, Review
from accounts.models import User
from django.contrib import messages
# from membership.forms import ReviewsForm

def information(request,user_n) :
    user = get_object_or_404(User, id=user_n)
    context ={"user" : user}
    return render(request,"information.html",context)

def recharge(request, user_n) :
    user = get_object_or_404(User, id=user_n)
    giftcard_list = Gift_card.objects.all()
    serial_list = [giftcard.serial_number for giftcard in giftcard_list]

    if request.POST["serial"].isdecimal():
        get_number =  int( request.POST["serial"] )
        if get_number in serial_list:
            for k in range(0,len(giftcard_list)):
                n = serial_list[k]
                if n == get_number:
                    user.point += giftcard_list[k].value
                    user.save()
                    break
            return redirect("membership:information", user_n)
        else:
            messages.add_message(request, messages.INFO, '존재하지 않는 번호입니다.')
            return redirect("membership:information", user_n)
    else:
<<<<<<< HEAD
        redirect
def history(request) :
    if request.method == "POST":
        return render(request, "history.html")

    else :
        return render(request, "history.html",{"history":[]})

=======
        messages.add_message(request, messages.INFO, '잘못된 입력입니다.')
        return redirect("membership:information", user_n)
>>>>>>> master

# -------------------근웅------------------
def history(request, user_n):
    user = get_object_or_404(User, id=user_n)
    user_histories = user.history_set.all().order_by('-id')
    return render(request, "history.html",{"histories": user_histories})


def r_create(request, history_id):
    if request.method == "POST":
        user_n = request.session["user_n"]
        history = get_object_or_404(History, id = history_id)
        comment = request.POST["review"]
        if True :   # 나중에 최소글자수 추가 할수도 있음
            Review.objects.create(user_id = user_n, history_id = history.id, comment = comment)
            return redirect("membership:history", user_n)
    else:
         return render(request,"create.html")
# ---------------------------------------
