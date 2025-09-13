from django.http import HttpResponse
from django.shortcuts import render,redirect

# Create your views here.
def index(request):
    return HttpResponse("欢迎使用")

def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return render(request,'user_add.html')

def tpl(request):
    name = "韩超"
    roles = ["管理员","CEO","保安"]
    user_info = {"name":"郭志","salary":100000,"role":"CTO"}
    return render(request,'tpl.html',{"n1":name,"n2":roles,"n3":user_info})

def news(request):

    return render(request,'news.html')

def somthing(request):
    print(request.method)
    print(request.GET)
    # return render(request,'somthing.html',{"title":"来了"})
    return redirect("https://www.baidu.com")

def login(request):
    if request.method == "GET":
        return render(request,'login.html')

    print(request.POST)
    username = request.POST.get("username")
    password = request.POST.get("password")

    if username == 'root' and password == '123':
        return redirect("/index/")

    return render(request,'login.html',{"error_message":"用户名或密码错误"})

from app01.models import UserInfo,Department,Role
def orm(request):
    # Department.objects.create(title='财务部')
    # Department.objects.create(title='销售部')
    # Department.objects.create(title='技术部')
    # UserInfo.objects.create(name='张三',password='123456',age=25)
    # UserInfo.objects.create(name='李四',password='123456',age=25)
    # UserInfo.objects.create(name='王五',password='123456')
    # UserInfo.objects.filter(name='张三').delete()
    # UserInfo.objects.all().delete()
    # row_obj = UserInfo.objects.filter(age=25).first()
    # print(row_obj.name,row_obj.age,row_obj.password)
    # for obj in data:
    #     print(obj.name,obj.age,obj.password)

    # print(data)
    # UserInfo.objects.filter(name='王五').update(age=18)

    return HttpResponse("添加成功")

def info_list(request):
    data_list = UserInfo.objects.all()
    print(data_list)

    return render(request,'info_list.html',{"data_list":data_list})

def info_add(request):
    if request.method == "GET":
        return render(request,'info_add.html')

    name = request.POST.get("user")
    password = request.POST.get("pwd")
    age = request.POST.get("age")
    UserInfo.objects.create(name=name,password=password,age=age)

    return redirect("/info/list/")

def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/info/list/")