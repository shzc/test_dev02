from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import requests
import json
# Create your views here.

def testcase_manage(request):
    return render(request,"testcase.html",{"type":"debug"})

def testcase_debug(request):
    '''测试用例的调试'''
    if request.method == "POST":
        url = request.POST.get("url","")
        moethd = request.POST.get("moethd","")
        header = request.POST.get("header","")
        type_ = request.POST.get("type","")
        parameter = request.POST.get("parameter","")

#转换参数，header单引号，捕捉错误
        json_par = parameter.replace("\'","\"")
        try:
            payload = json.loads(json_par)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result":"参数类型有误"})

        json_header = header.replace("\'", "\"")
        try:
            header = json.loads(json_header)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"result":"header类型有误"})

        # print("url",url)
        # print("moethd",moethd)
        # print("header",header)
        # print("type",type)
        # print("parameter",type(parameter))

        if moethd == "get":
            if header == "":
                r = requests.get(url,params=payload)
                print("结果",r.json())
            else:
                r = requests.get(url, params=payload,headers=header)
                print("结果", r.json())

        if moethd == "post":
            if type_ == "from":
                if header == "":
                    r = requests.post(url, data=payload)
                    print(r.text)
                else:
                    r = requests.post(url, data=payload, headers=header)
                    print(r.text)

            if type_ == "json":
                if header == "":
                    r = requests.post(url, json=payload)
                    print(r.text)
                else:
                    r = requests.post(url, json=payload, headers=header)
                    print(r.text)

        return JsonResponse({"result":r.text})
    else:
        return JsonResponse({"result":"请求方法错误"})


def testcase_assert(request):
    '''测试用例的断言'''

    if request.method == "POST":
        result_text = request.POST.get("result", "")
        assert_text = request.POST.get("assert", "")
        assert_type = request.POST.get("assert_type", "")

        if result_text == "" or assert_text == "":
            return JsonResponse({"result": "断言的文本不能为空"})

        # 包含
        if assert_type == "contains":
            if assert_text not in result_text:
                return JsonResponse({"result": "断言失败"})
            else:
                return JsonResponse({"result": "断言成功"})
        # 匹配
        elif assert_type == "mathches":
            if assert_text != result_text:
                return JsonResponse({"result": "断言失败"})
            else:
                return JsonResponse({"result": "断言成功"})



    else:
        return JsonResponse({"result":"请求方法错误"})


