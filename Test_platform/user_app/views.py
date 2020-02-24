from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

def say_hello(request):
    input_name = request.GET.get('name',"")
    # talk = []
    # for i in range(3):
    #     talk.append( "hello," + name )
    if input_name == "":
        return HttpResponse("请求输入?name=name")
    return render(request,"index.html",{"name":input_name})

def index(request):
    """
    登录的首页
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "index.html")
    else:
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        if username == "" or password == "":
            return render(request, "index.html", {
                "error": "用户名密码为空"})

        #使用django自带校验用户名密码方法authenticate实线异常判断
        user = auth.authenticate(username=username,password=password)
        if user is  None:
            return render(request, "index.html", {
                "error": "用户名密码错误"})
        else:
            #记录用户的登录的状态(只有在登录状态下才能到manage页面)，框架自带的auth下的login方法
           auth.login(request,user)
            #登录成功使用HttpResponseRedirect重定向
           return HttpResponseRedirect("/project/")

#处理用户的退出
def logout(request):
    auth.logout(request)#清除浏览器缓存
    return HttpResponseRedirect("/index/")#重新指到index页面

