from django.urls import path
from testcase_app import views

urlpatterns = [
    #用例管理
    path('',views.testcase_manage),
    path('debug',views.testcase_debug),
    path('assert',views.testcase_assert),

]
