# Generated by Django 4.2 on 2023-04-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_fiyat_currency_alter_product_fiyat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='olusturulma_tarihi',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
