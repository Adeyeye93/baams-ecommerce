# Generated by Django 4.0.2 on 2024-06-18 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_remove_product_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
