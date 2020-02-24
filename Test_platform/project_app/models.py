from django.db import models

# Create your models here.
# ORM像操作对象一样操作数据库

class Project(models.Model):
    """
    项目表
    """
    name = models.CharField("名称",max_length=50,null=False)
    describe = models.TextField("描述",default="")
    status = models.BooleanField("状态",default=1)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField("创建时间",auto_now_add=True)#auto_now_add自动添加创建时间

    # 在admin后台中Module和Project关联的名称
    def __str__(self):
        return self.name
