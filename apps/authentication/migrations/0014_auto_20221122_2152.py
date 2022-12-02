# Generated by Django 3.2.14 on 2022-11-22 13:52

import common.db.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0013_connectiontoken_protocol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='connectiontoken',
            old_name='account_username',
            new_name='login'
        ),
        migrations.AlterField(
            model_name='connectiontoken',
            name='login',
            field=models.CharField(max_length=128, verbose_name='Login account'),
        ),
        migrations.AddField(
            model_name='connectiontoken',
            name='username',
            field=models.CharField(default='', max_length=128, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='connectiontoken',
            name='secret',
            field=common.db.fields.EncryptCharField(default='', max_length=128, verbose_name='Secret'),
        ),
    ]
