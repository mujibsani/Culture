# Generated by Django 3.2.4 on 2021-06-26 11:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('culture_blog', '0005_alter_post_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 26, 11, 40, 15, 607067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='media/%y'),
        ),
    ]
