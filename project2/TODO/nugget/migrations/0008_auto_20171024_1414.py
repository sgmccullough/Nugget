# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 18:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nugget', '0007_auto_20171024_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='battle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('battle_id', models.IntegerField(help_text='Unique Battle ID')),
                ('net_coins', models.DecimalField(decimal_places=0, help_text='Coins won or lost', max_digits=10)),
            ],
            options={
                'ordering': ['battle_id', 'nug_id', 'net_coins'],
            },
        ),
        migrations.CreateModel(
            name='nug_ids',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'ordering': ['nug_id'],
            },
        ),
        migrations.RenameField(
            model_name='nugget',
            old_name='atributes',
            new_name='attributes',
        ),
        migrations.AddField(
            model_name='nuggetattribute',
            name='nug_health',
            field=models.IntegerField(default='100', help_text='health of nugget'),
        ),
        migrations.AddField(
            model_name='nug_ids',
            name='nug_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nugget.Nugget'),
        ),
        migrations.AddField(
            model_name='battle',
            name='nug_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nugget.Nugget'),
        ),
        migrations.AddField(
            model_name='battle',
            name='opponent_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nugget.nug_ids'),
        ),
    ]
