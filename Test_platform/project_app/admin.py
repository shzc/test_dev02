from django.contrib import admin
from project_app.models import Project
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','describe','status','create_time']
    search_fields = ['name']#admin后台增加搜索
    list_filter = ['status']#admin后台增加过滤状态



#注册admin模型，
admin.site.register(Project,ProjectAdmin)
