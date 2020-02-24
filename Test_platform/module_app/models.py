from django.db import models
from project_app.models import Project

class Module(models.Model):
    """
    创建一张模块表
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)#关联Project项目,删除项目模块一起删除on_delete=models.CASCADE
    name = models.CharField("名称",max_length=50, null=False)
    describe = models.TextField("描述",default="")
    status = models.BooleanField("状态",default=1)
    create_time = models.DateTimeField("创建时间",auto_now_add=True)  # auto_now_add自动

    # 在admin后台中Module和Project关联的名称
    def __str__(self):
        return self.name