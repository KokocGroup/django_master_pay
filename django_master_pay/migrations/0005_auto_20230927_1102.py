# Generated by Django 2.2 on 2023-09-27 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_master_pay', '0004_auto_20210726_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Ожидает'), (1, 'Выплачивается'), (2, 'Выплачен частично'), (5, 'Ошибка'), (4, 'Выплачен'), (3, 'Отменен пользователем'), (6, 'Неисполнимый')], default=0, verbose_name='Статус'),
        ),
    ]