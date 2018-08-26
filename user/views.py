from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password

from user.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            # 创建user对象,但不提交到数据库
            user = form.save(commit=False)
            # 密码加密保存
            user.password = make_password(user.password)
            user.save()
            return redirect('/user/info/')
        else:
            return render(request, 'register.html', {'error': form.errors})
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html', {})


def logout(request):
    return render(request, 'logout.html', {})


def user_info(request):
    return render(request, 'user_info.html', {})


