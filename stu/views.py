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


# 显示所有班级信息
def showall_view(request):
    # 查询班级表中的所有数据
    cls = Clazz.objects.all()

    return render(request, 'showall.html', {'cls': cls})


# 显示当前班级下的所有学生信息
def getstu_view(request):
    # 1获取班级编号
    cno = request.GET.get('cno', '')
    # 2根据班级编号查询学生信息
    cno = int(cno)
    stus = Clazz.objects.get(cno=cno).student_set.all()
    return render(request, 'stulist.html', {'stus': stus})
