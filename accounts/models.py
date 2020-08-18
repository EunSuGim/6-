from django.db import models


class User(models.Model):
    user_name = models.CharField('이름', max_length=10)
    user_id = models.CharField('아이디', max_length=20, unique=True)
    password = models.CharField('비밀번호', max_length=100)
    phone_num = models.CharField('전화번호', max_length=11, default=0)
    point = models.IntegerField('마일리지', default=0)

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "user"

