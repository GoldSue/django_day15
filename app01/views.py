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
