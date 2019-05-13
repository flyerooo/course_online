from datetime import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    SEX_MALE = 1
    SEX_FEMALE = 2
    SEX_UNKNOWN = 0
    SEX_ITEMS = [
        (SEX_MALE, '男'),
        (SEX_FEMALE, '女'),
        (SEX_UNKNOWN, '未知'),
    ]
    nick_name = models.CharField(max_length=50, verbose_name="昵称", default="")
    birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    gender = models.IntegerField(choices=SEX_ITEMS, verbose_name='性别', default=SEX_FEMALE)
    address = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to="image/%Y/%m", default="image/default.png", max_length=100)

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username

    def unread_nums(self):
        # 获取用户未读消息的数量
        from operation.models import UserMessage
        return UserMessage.objects.filter(user=self.id, has_read=False).count()


class EmailVerifyRecord(models.Model):
    TYPE_REGISTER = 1
    TYPE_FORGET = 0
    TYPE_UPDATE_EMAIL = 2
    SEND_TYPE = [
        (TYPE_REGISTER, u"注册"),
        (TYPE_FORGET, u"找回密码"),
        (TYPE_UPDATE_EMAIL, u"修改邮箱"),
    ]
    code = models.CharField(max_length=20, verbose_name=u"验证码")
    email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    send_type = models.IntegerField(verbose_name="验证码类型", choices=SEND_TYPE)
    send_time = models.DateTimeField(verbose_name="发送时间", default=datetime.now)

    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name=u"标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name=u"轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name=u"访问地址")
    index = models.IntegerField(default=100, verbose_name=u"顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name
