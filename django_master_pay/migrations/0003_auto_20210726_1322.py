# Generated by Django 2.2.2 on 2021-07-26 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_master_pay', '0002_auto_20210721_1229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Ожидает'), (1, 'Выплачивается'), (2, 'Выплачен частично'), (5, 'Ошибка'), (4, 'Выплачен'), (3, 'Отменен пользователем')], default=0, max_length=100, verbose_name='Статус'),
        ),
    ]
