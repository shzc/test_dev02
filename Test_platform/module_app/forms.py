from django import forms
from module_app.models import Module


# form表单渲染前端模块编辑页面
class ModuleForm(forms.ModelForm):

    class Meta:
        model = Module
        fields = ["project","name","describe"]