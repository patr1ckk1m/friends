# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-01 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='alias',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiverequest', to='firstapp.User'),
        ),
        migrations.AddField(
            model_name='friend',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sendrequest', to='firstapp.User'),
        ),
    ]
