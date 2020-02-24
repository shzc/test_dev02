from django.urls import path
from project_app import views

urlpatterns = [
    #项目管理
    path('',views.project_manage),
    path('add_project/', views.add_project),
    path('edit_project/<int:pid>/', views.edit_project),  # <int:pid>编辑页面的对应页数
    path('delete_project/<int:pid>/', views.delete_project),

    #接口
    path('get_project_list/', views.get_project_list),

]
