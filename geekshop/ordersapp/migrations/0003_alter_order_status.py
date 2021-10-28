# Generated by Django 3.2.8 on 2021-10-28 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersapp', '0002_order_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('FM', 'формируется'), ('STP', 'отпарвленно в обработку'), ('PD', 'Оплачено'), ('PRD', 'обрабатывается'), ('RDY', 'готов к выдачи'), ('CNC', 'отмена заказа')], default='FM', max_length=3, verbose_name='Статус'),
        ),
    ]
