from django import forms
from project_app.models import Project

# form表单渲染前端项目编辑页面

class ProjectForm(forms.ModelForm):
    # name = forms.CharField(label="项目", max_length=100)
    # describe = forms.CharField(label="描述", widget=forms.Textarea)
    # status = forms.BooleanField(label="状态", required=False)

    class Meta:
        model = Project
        fields = ["name","describe","status"]