from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
SEX_CHOICES = (
    (0, '男'),
    (1, '女'),
)
ROLE_CHOICES = (
    (0, 'buy'),
    (1, 'sale'),
    (2, 'admin'),
)
BANK_CHOICES = (
    (0, '中国工商银行'),
    (1, '中国农业银行'),
    (2, '中国邮政银行'),
    (3, '中国建设银行'),
    (4, '盛京银行'),
)
class User(AbstractUser):
    # username = models.CharField(max_length=30, verbose_name="用户名", null=False)
    # password = models.CharField(max_length=50, verbose_name="密码", null=False)
    realname = models.CharField(max_length=30, verbose_name="真实姓名", null=False)
    iden = models.CharField(max_length=18, verbose_name="身份证号", null=False)
    ads = models.CharField(max_length=30, verbose_name="地址", null=False)
    uphone = models.CharField(max_length=11, verbose_name="手机号", null=False)
    sex = models.IntegerField(choices=SEX_CHOICES, verbose_name="性别", default=0)
    role = models.IntegerField(choices=ROLE_CHOICES, verbose_name="角色", default=0)
    isActive = models.BooleanField(default=False, verbose_name="激活状态")
    isBan = models.BooleanField(default=False, verbose_name="是否禁用")

    def __str__(self):
        return self.realname

    class Meta:
        db_table = "user_info"
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name

class BankInfo(models.Model):
    cardNo = models.CharField(verbose_name="卡号", max_length=30, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 删除关联数据,与之关联也删除
    cpwd = models.CharField(verbose_name="交易密码", max_length=200, null=False)
    bank = models.IntegerField(verbose_name="开户行", choices=BANK_CHOICES)
    isDelete = models.BooleanField(verbose_name="是否删除", default=False)

    def __str__(self):
        return self.user.username
    class Meta:
        db_table = "bank_info"
        verbose_name = "银行卡信息表"
        verbose_name_plural = verbose_name




