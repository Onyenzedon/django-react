from django.db import models
from decimal import Decimal

# Create your models here.


# class Invoice(models.Model):
#     Description = models.CharField(max_length=100)
#     Brand = models.CharField(max_length=100)
#     Quantity = models.PositiveIntegerField()
#     Value = models.CharField(max_length=100)
#     Unit_Price = models.PositiveIntegerField()
#     Total_Price = models.DecimalField(max_digits=16, decimal_places=2, default=0.0)

#     def __str__(self):
#         return self.Description

class Invoice(models.Model):
    Description = models.CharField(max_length=100, default="")
    Brand = models.CharField(max_length=100, default="")
    Quantity = models.PositiveIntegerField()
    Value = models.CharField(max_length=100, default="")
    Unit_Price = models.PositiveIntegerField()
    # Total_Price = models.DecimalField(max_digits=16, decimal_places=2, default=0.0)

    def __str__(self):
        return self.Description