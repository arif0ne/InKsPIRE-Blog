# Generated by Django 5.1.dev20240306045047 on 2024-03-31 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_rename_comments_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
