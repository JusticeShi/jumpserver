# Generated by Django 3.2.14 on 2022-11-16 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ops', '0030_auto_20221116_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='chdir',
            field=models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Chdir'),
        ),
        migrations.AddField(
            model_name='job',
            name='comment',
            field=models.CharField(blank=True, default='', max_length=1024, null=True, verbose_name='Comment'),
        ),
        migrations.AddField(
            model_name='job',
            name='timeout',
            field=models.IntegerField(default=60, verbose_name='Timeout (Seconds)'),
        ),
    ]
