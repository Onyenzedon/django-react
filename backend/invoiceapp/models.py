from django.db import models

# Create your models here.


class InvoiceApp(models.Model):
    Description = models.CharField(max_length=100, default="")
    Brand = models.CharField(max_length=100, default="")
    Quantity = models.PositiveIntegerField()
    Value = models.CharField(max_length=100, default="")
    Unit_Price = models.PositiveIntegerField()
    Total_Price = models.DecimalField(max_digits=16, decimal_places=2, default=0.0, null=True, blank=True)

    def __str__(self):
        return self.Description