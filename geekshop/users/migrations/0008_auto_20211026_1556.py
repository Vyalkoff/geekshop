# Generated by Django 3.2.8 on 2021-10-26 15:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20211026_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='activation_key_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 10, 28, 15, 56, 28, 369328, tzinfo=utc), null=True),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagline', models.CharField(blank=True, max_length=128, verbose_name='Тэги')),
                ('about', models.TextField(blank=True, null=True, verbose_name='О себе')),
                ('gender', models.CharField(blank=True, choices=[('M', 'М'), ('W', 'Ж')], max_length=5, verbose_name='Пол')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
