from django.shortcuts import render, get_object_or_404,redirect,HttpResponseRedirect,reverse
from membership.models import Gift_card
from accounts.models import User

def information(request,user_n) :
    user = get_object_or_404(User, id=user_n)
    context ={"user" : user}
    return render(request,"information.html",context)

def recharge(request, user_n) :
    user = get_object_or_404(User, id=user_n)
    giftcard_list = Gift_card.objects.all()
    get_number =  int( request.POST["serial"] )
    for k in range(0,len(giftcard_list)):
        n = giftcard_list[k].serial_number
        if n == get_number:
            user.point += giftcard_list[k].value
            user.save()
            break
        # return HttpResponseRedirect(reverse('membership:information', args=(user_n,)))
    return redirect("membership:information", user_n)

def history(request) :
    return render(request, "history.html",{"history":[]})


