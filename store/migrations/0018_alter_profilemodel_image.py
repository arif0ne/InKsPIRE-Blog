# Generated by Django 5.1.dev20240306045047 on 2024-03-25 05:50

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_profilemodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profileImg/', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])]),
        ),
    ]