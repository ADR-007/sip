# -*- coding: utf-8 -*-
# Generated by Django 1.11a1 on 2017-08-28 17:51
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassworddata',
            name='token',
            field=models.CharField(blank=True, default='05878a07b9704e989da31b4b212c3168d4e205710f024cf2b8434ed2467f67ba', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, default='100265ed90804ad0815fd4027167389df6fb1517577c48fa9f54c1a73e15ae68', max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]