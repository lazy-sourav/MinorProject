# Generated by Django 5.1.3 on 2024-11-09 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_products_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='dosage',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/'),
        ),
        migrations.AddField(
            model_name='products',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/'),
        ),
        migrations.AddField(
            model_name='products',
            name='prescription_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/products/'),
        ),
    ]