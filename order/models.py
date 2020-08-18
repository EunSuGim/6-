from django.db import models


class Coffee(models.Model):
    cd = models.IntegerField()
    name = models.CharField(max_length=100)
    kcal = models.IntegerField()
    sat_fat = models.IntegerField(db_column='sat_FAT')
    protein = models.IntegerField()
    fat = models.IntegerField()
    trans_fat = models.IntegerField(db_column='trans_FAT')
    sodium = models.IntegerField()
    sugars = models.IntegerField()
    caffeine = models.IntegerField()
    cholesterol = models.IntegerField()
    chabo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Coffee'

    def __str__(self):
        return self.name
