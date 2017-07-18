from django.contrib.auth import authenticate, \
                                login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from . import views


# 로그인, 로그아웃, 회원가입
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        context = {'error_messages': ''}
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return render(request, 'blog/index.html' )
        else:
            context['error_messages'] = '다시 로그인하세요. 잘못된 입력입니다.'
            return render(request, 'user/login.html', context)
    else:
        return render(request, 'user/login.html')


def logout(request):
    auth_logout(request)
    return redirect('blog:index')


def sign_up(request):
    pass
