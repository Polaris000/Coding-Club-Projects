# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-02 11:18
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lev_num', models.IntegerField(default=1)),
                ('is_emer_red', models.BooleanField(default=False)),
                ('is_emer_blue', models.BooleanField(default=False)),
                ('is_emer_green', models.BooleanField(default=False)),
                ('is_emer_yellow', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prob_num', models.IntegerField(blank=True, default=None)),
                ('answer', models.CharField(max_length=1000)),
                ('prob_num_diam', models.IntegerField(default=50)),
                ('prob_hint', models.CharField(max_length=1000)),
                ('prob_help', models.CharField(max_length=1000)),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Qriousapp.Level')),
            ],
        ),
        migrations.CreateModel(
            name='CustUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('rank', models.IntegerField(blank=True, null=True)),
                ('lev_num', models.IntegerField(default=1)),
                ('num_diamonds', models.IntegerField(default=100)),
                ('is_emer_red', models.BooleanField(default=False)),
                ('is_emer_blue', models.BooleanField(default=False)),
                ('is_emer_green', models.BooleanField(default=False)),
                ('is_emer_yellow', models.BooleanField(default=False)),
                ('num_emers', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
