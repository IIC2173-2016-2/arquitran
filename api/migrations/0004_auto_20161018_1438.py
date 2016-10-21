# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-18 14:38
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161013_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default=Decimal('0'), default_currency='CLP', max_digits=10, verbose_name='Money to exchange'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='app',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ApplicationToken'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='kredit_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.KreditCard'),
        ),
    ]