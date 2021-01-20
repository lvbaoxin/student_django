from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import *


def index_view(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        # 接收请求参数
        sname = request.POST.get("sname", '')
        cname = request.POST.get("clsname", '')
        coursnames = request.POST.getlist("coursname", [])
        # 将数据注册到数据库
        flag = registerStu(sname, cname, *coursnames)
        if flag:
            return HttpResponse("注册成功")
        return HttpResponse("注册失败")
