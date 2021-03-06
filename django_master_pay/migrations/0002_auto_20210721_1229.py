# Generated by Django 2.2.2 on 2021-07-21 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_master_pay', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='error',
            field=models.TextField(blank=True, null=True, verbose_name='Ошибка автоматической выплаты'),
        ),
        migrations.AddField(
            model_name='payment',
            name='partner_id',
            field=models.CharField(default=0, max_length=250, verbose_name='Индефикатор партнера в MasterPay'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[(0, 'Ожидает'), (1, 'Выплачивается'), (2, 'Выплачен частично'), (5, 'Ошибка'), (4, 'Выплачен'), (3, 'Отменен пользователем')], default=0, max_length=100, verbose_name='Статус'),
        ),
    ]
