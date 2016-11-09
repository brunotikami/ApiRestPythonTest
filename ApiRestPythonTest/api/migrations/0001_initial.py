# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-08 02:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeiraLivre',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('DISTRITO', models.CharField(db_index=True, max_length=80)),
                ('SUBPREFE', models.CharField(max_length=45)),
                ('REGIAO5', models.CharField(db_index=True, max_length=45)),
                ('REGIAO8', models.CharField(max_length=45)),
                ('NOME_FEIRA', models.CharField(db_index=True, max_length=150)),
                ('REGISTRO', models.CharField(db_index=True, max_length=50)),
                ('LOGRADOURO', models.CharField(max_length=155)),
                ('NUMERO', models.CharField(max_length=45)),
                ('BAIRRO', models.CharField(db_index=True, max_length=150)),
                ('REFERENCIA', models.CharField(max_length=45)),
            ],
        ),
    ]
