# Generated by Django 4.0.2 on 2022-03-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoiceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceapp',
            name='Total_Price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=16, null=True),
        ),
    ]
