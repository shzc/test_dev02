from django.shortcuts import render
from django.contrib.auth.decorators import login_required #django里面的一个装饰器
from project_app.models import Project
from django.http import HttpResponseRedirect, JsonResponse
from project_app.forms import ProjectForm



@login_required#只有在登录状态下才能到manage页面
def project_manage(request):
    """
    登录成功跳转默认管理页面
    项目管理页面
    """
    project_all = Project.objects.all()#查询出所有项目
    return render(request,"project.html",{"projects":project_all,
                                          "type":"list"})


@login_required
def add_project(request):
    """
    添加项目
    """
    # print("请求方法",request.method)
    if request.method == "GET":
        return render(request,"project.html",{"type":"add"})
    elif request.method == "POST":
        name = request.POST.get('name', "")
        describe = request.POST.get('describe', "")
        status = request.POST.get('status', "")
        if name == "":
            return render(request, "project.html", {"type": "add",
                                                    "name_error":"项目名称不能为空"})
        Project.objects.create(name=name, describe=describe, status=status)
        return HttpResponseRedirect("/project/")  # 创建完项目跳转



@login_required
def edit_project(request,pid):
    """
    编辑项目
    """
    # print("请求方法",request.method)
    if request.method == "GET":

        if pid:
            p = Project.objects.get(id=pid)
            project_form = ProjectForm(instance=p)
            return render(request,"project.html",{"type":"edit",
                                                  "form":project_form,
                                                  "id":pid})
# 编辑完数据更新数据
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            status = form.cleaned_data["status"]

            p = Project.objects.get(id=pid)
            p.name = name
            p.describe = describe
            p.status = status
            p.save()
        return HttpResponseRedirect("/project/")

def delete_project(request,pid):
    """
    删除项目
    """
    print("delete project",pid)
    if request.method == "GET":
        try:
            project = Project.objects.get(id=pid)

        except Project.DoesNotExist:
            print("你删除的项目不存在")
            return HttpResponseRedirect("/project/")
        else:
            project.delete()
        return HttpResponseRedirect("/project/")
    else:
        return HttpResponseRedirect("/project/")


def get_project_list(request):
    '''获取项目列表'''
    if request.method == "GET":
        projects = Project.objects.all()
        project_list = []
        for pro in projects:
            project_dict = {
                "id":pro.id,
                "name":pro.name,
            }
            project_list.append(project_dict)


        return JsonResponse({"status":10200,
                             "message":"请求成功",
                             "data":project_list})
    else:
        return JsonResponse({"status":10101,
                             "message": "请求方法错误"})
