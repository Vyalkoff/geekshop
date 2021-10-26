# Generated by Django 3.2.8 on 2021-10-26 15:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_user_activation_key_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='user',
            name='activation_key_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 28, 15, 2, 9, 64023, tzinfo=utc), null=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
