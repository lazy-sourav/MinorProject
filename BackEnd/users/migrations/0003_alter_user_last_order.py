# Generated by Django 5.1.3 on 2024-11-10 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_address_alter_user_age_alter_user_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_order',
            field=models.TextField(blank=True, null=True),
        ),
    ]
