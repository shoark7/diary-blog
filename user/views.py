from django.contrib.auth import authenticate, \
                                login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from . import views
from .forms import BlogUserForm
from .models import BlogUser
from blog.views import index


# 로그인, 로그아웃, 회원가입
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        context = {'error_messages': ''}
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            request.user = user
            # return render(request, 'blog/index.html')
            return redirect('blog:index')
        else:
            context['error_messages'] = '다시 로그인하세요. 잘못된 입력입니다.'
            return render(request, 'user/login.html', context)
    else:
        return render(request, 'user/login.html')


def logout(request):
    auth_logout(request)
    return redirect('blog:index')


def sign_up(request):
    ## This is for previous way
    # if request.method == 'POST':
        # username = request.POST.get('username')
        # password1 = request.POST.get('password1')
        # password2 = request.POST.get('password2')
        # name = request.POST.get('name')
        # phonenumber = request.POST.get('phonenumber')
        # sex = request.POST.get('sex')

    #     if password1 != password2:
    #         context = {'error_messages': '비밀번호가 다릅니다.'}
    #         return render(request, 'user/sign_up.html', context)
    #     try:
    #         user = BlogUser.objects.create_user(username=username,
    #                         password=password1,
    #                         name=name,
    #                         phonenumber=phonenumber,
    #                         sex=sex)
    #     except:
    #         context = {'error_messages': '뭔가 문제가..'}
    #         return render(request, 'user/sign_up.html', context)
    #     else:
    #         user = authenticate(username=username, password=password1)
    #         auth_login(request, user)
    #         # return redirect('blog:index')
    #         return render(request, 'blog/index.html')
    # else:
    #     return render(request, 'user/sign_up.html')

    # 1. Form way
    if request.method == 'POST':
        form = BlogUserForm(request.POST, initial={'error_messages': ''})
        if form.is_valid():
            cleaned_data = form.cleaned_data
            username = cleaned_data.get('username')
            password1 = cleaned_data.get('password1')
            password2 = cleaned_data.get('password2')
            name = cleaned_data.get('name')
            phonenumber = cleaned_data.get('phonenumber')
            sex = cleaned_data.get('sex')

            try:
                user = BlogUser.objects.create_user(username=username,
                                                    password=password1,
                                                    name=name,
                                                    phonenumber=phonenumber,
                                                    sex=sex,)
            except:
                form['error_messages'] = '문제가 있습니다'
            else:
                user = authenticate(username=username, password=password1)
                auth_login(request, user)
                return render(request, 'blog/index.html')
    else:
        form = BlogUserForm()

    return render(request, 'user/sign_up.html', {'form': form})
