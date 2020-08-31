from django.db import models
from accounts.models import User
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

def min_length_10_validator(value):
    if len(value) < 10 :
        raise forms.ValidationError('최소 10자 이상 입력해주세요.')

class Gift_card(models.Model):
    name = models.CharField(max_length=10)
    value = models.IntegerField()
    serial_number = models.IntegerField()

    def __str__(self):
        return self.name

class History(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField('상품명',max_length=20,null=True)
    quantity = models.IntegerField('수량',default=0)
    total = models.IntegerField('총가격',default=0)
    order_date = models.DateField(auto_now=True)
    cd = models.IntegerField('cd',null=True)
    category = models.CharField('카테고리',max_length=20,null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    create_date = models.DateField(auto_now=True)
    comment = models.TextField("글내용",max_length=1000, validators=[min_length_10_validator])
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return self.comment
