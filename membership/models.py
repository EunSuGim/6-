from django.db import models
from accounts.models import User

class Gift_card(models.Model):
    name = models.CharField(max_length=10)
    value = models.IntegerField()
    serial_number = models.IntegerField()

    def __str__(self):
        return self.name

class Histories(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField('상품명',max_length=20,null=True)
    quantity = models.IntegerField('수량',default=0)
    total = models.IntegerField('총가격',default=0)
    order_date = models.DateField(auto_now=True)
    cd = models.IntegerField('cd',null=True)
    category = models.CharField('카테고리',max_length=20,null=True)

    def __str__(self):
        return self.name

