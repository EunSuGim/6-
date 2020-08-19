from django.db import models


#coffee,desserts,goods 모델 추가 김은수
class Coffee(models.Model):
    text = models.CharField(max_length=100)
    cd = models.IntegerField()
    name = models.CharField(max_length=20)
    allergy = models.CharField(max_length=100, blank=True, null=True)
    kcal = models.IntegerField()
    sat_fat = models.IntegerField(db_column='sat_FAT')  # Field name made lowercase.
    protein = models.IntegerField()
    fat = models.IntegerField()
    trans_fat = models.IntegerField(db_column='trans_FAT')  # Field name made lowercase.
    sodium = models.IntegerField()
    sugars = models.IntegerField()
    cholesterol = models.IntegerField()
    chabo = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Coffee'



class Desserts(models.Model):
    text = models.CharField(max_length=100)
    cd = models.IntegerField()
    name = models.CharField(max_length=20)
    gram = models.IntegerField()
    allergy = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Desserts'



class Goods(models.Model):
    text = models.CharField(max_length=100)
    cd = models.IntegerField()
    name = models.CharField(max_length=20)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Goods'

class carts(models.Model):
    pass
