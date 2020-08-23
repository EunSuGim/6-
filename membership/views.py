from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect,reverse
from membership.models import Gift_card
from accounts.models import User
from django.contrib import messages

def information(request,user_n) :
    user = get_object_or_404(User, id=user_n)
    context ={"user" : user}
    return render(request,"information.html",context)

def recharge(request, user_n) :
    user = get_object_or_404(User, id=user_n)
    giftcard_list = Gift_card.objects.all()
    serial_list = [giftcard.serial_number for giftcard in giftcard_list]

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

def history(request) :
    return render(request, "history.html",{"history":[]})


