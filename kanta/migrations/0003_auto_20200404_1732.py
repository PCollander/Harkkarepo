# Generated by Django 3.0.5 on 2020-04-04 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanta', '0002_auto_20200404_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onnettomuus',
            name='kunta',
        ),
        migrations.AddField(
            model_name='onnettomuus',
            name='Kunta',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='onnettomuus',
            name='Kuntasel',
            field=models.CharField(max_length=100),
        ),
    ]
