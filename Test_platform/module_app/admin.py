from django.contrib import admin
from module_app.models import Module
# Register your models here.

class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name','describe','status','create_time','project']
    search_fields = ['name']
    list_filter = ['project']

#注册admin模型，
admin.site.register(Module,ModuleAdmin)