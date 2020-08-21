from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import User


def log_in(request):
    # post 방식
    if request.method == 'POST':
        user_id = request.POST['user_id']
        password = request.POST['password']
        if User.objects.filter(user_id=user_id).exists() == True: # user_id 가 일치하면 True
            user = get_object_or_404(User, user_id=user_id)  # 변수 선언
            if user.password == password:
                request.session['user_id'] = user_id
                request.session['check'] = 1
                request.session['user_n'] = user.id
            else:
                print('비밀번호 틀림')

        else:
            print('아이디 존재X')

        return redirect('/')
    # get 방식
    return render(request, 'login.html')


def sign_up(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        print(request.POST)
        user_id = request.POST['user_id']  # 변수 선언
        if User.objects.filter(user_id=user_id).exists() == False:  # user_id 중복이 되면 False
        # password와 confirm에 입력된 값이 같다면
            if request.POST['password1'] == request.POST['password2']:
                # user 객체를 새로 생성
                user = User(user_id=request.POST['user_id'], password=request.POST['password1'],
                            user_name=request.POST['user_name'], phone_num=request.POST['phone_num'])
                user.save()
                request.session['user_id'] = user_id
                request.session['check'] = 1    # 로그인 성공시 화면 넘어가기


                return redirect('/')
        else:
            print('이미존재하는 아이디입니다')
            return redirect('/accounts/signup/')
    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    return render(request, 'signup.html')


def log_out(request):
    request.session['check'] = 0
    del request.session['user_id']

    return redirect('/')


def cash(request):
    if request.method == 'POST':
        user = get_object_or_404(User, user_id=request.session['user_id'])
        user.point += int(request.POST['cash'])
        user.save()
        return redirect('/')

    return render(request, 'cash.html')