# Generated by Django 5.1.3 on 2024-11-05 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.URLField(max_length=600, null=True),
        ),
    ]