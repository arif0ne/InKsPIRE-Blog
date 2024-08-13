# Generated by Django 5.0.4 on 2024-04-27 05:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0022_alter_comment_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-published_in',)},
        ),
        migrations.AddField(
            model_name='comment',
            name='published_in',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
