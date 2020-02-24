from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required #django里面的一个装饰器
from module_app.models import Module
from module_app.forms import ModuleForm


@login_required
def module_manage(request):
    """
    模块管理页面
    """
    if request.method == "GET":
        module_all = Module.objects.all()
        return render(request,"module.html", {"modules":module_all,
                                              "type":"list"})

def add_module(request):
    """
    添加模块
    """
    # print("请求方法",request.method)
    # 获取模块页面
    if request.method == "GET":
        module_form = ModuleForm()
        return render(request, "module.html", {"form":module_form,
                                                "type": "add"})

    # 模块页面添加到数据库
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data["project"]
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            Module.objects.create(project=project,name=name,describe=describe)
            return HttpResponseRedirect("/module/")


def edit_module(request,mid):
    """
    编辑模块
    """
    if request.method == "GET":
        module = Module.objects.get(id=mid)
        module_form = ModuleForm(instance=module)
        return render(request, "module.html", {"form":module_form,
                                                "type": "edit",
                                               "id":module.id})

    # 模块页面添加到数据库
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data["project"]
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]

            m = Module.objects.get(id=mid)
            m.name = name
            m.describe = describe
            m.project = project
            m.save()
            return HttpResponseRedirect("/module/")

def delete_module(request,mid):
    """
    删除模块
    """
    if request.method == "GET":
        try:
            module = Module.objects.get(id=mid)

        except Module.DoesNotExist:
            print("你删除的项目不存在")
            return HttpResponseRedirect("/project/")
        else:
            module.delete()
        return HttpResponseRedirect("/module/")
    else:
        return HttpResponseRedirect("/module/")