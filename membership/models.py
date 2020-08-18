from django.db import models

class Gift_card(models.Model) :
    name = models.CharField(max_length=10)
    value = models.IntegerField()
    serial_number = models.IntegerField()

    def __str__(self):
        return self.name
