from django.shortcuts import render,HttpResponse
import random
from user.models import User
# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request,'user/login.html')
    else:
        zh = request.POST.get('zh').strip()
        mm = request.POST.get('mm').strip()
        if zh == "" or mm == "":
            return render(request,'user/login.html',{'err':'账号或密码必须填写'})
        else:
            try:
                User.objects.get(name = zh,pwd=mm)
                return HttpResponse('登录成功')
            except:
                return render(request, 'user/login.html', {'err': '账号或密码错误'})
def register(request):
    if request.method == 'GET':
        return render(request,'user/regist.html')
    else:
        zh = request.POST.get('zh').strip()
        mm = request.POST.get('mm').strip()
        if zh == "" or mm == "":
            return render(request,'user/regist.html',{'err':'账号或密码必须填写'})
        else:
            try:
                User.objects.create(name = zh,pwd = mm)
                return HttpResponse('注册成功')
            except:
                return render(request, 'user/regist.html', {'err': '注册失败'})

