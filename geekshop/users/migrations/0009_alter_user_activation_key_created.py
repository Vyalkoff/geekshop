# Generated by Django 3.2.8 on 2021-10-28 16:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20211026_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 30, 16, 31, 15, 715635, tzinfo=utc), null=True),
        ),
    ]
