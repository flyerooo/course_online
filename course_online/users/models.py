from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    SEX_ITEMS = [
        (1, '男'),
        (2, '女'),
        (0, '未知'),
    ]
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.IntegerField(choices=SEX_ITEMS, verbose_name='性别')
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    # def unread_nums(self):
    #     # 获取用户未读消息的数量
    #     from operation.models import UserMessage
    #     return UserMessage.objects.filter(user=self.id, has_read=False).count()
