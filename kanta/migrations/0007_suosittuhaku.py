# Generated by Django 3.0.5 on 2020-04-27 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanta', '0006_auto_20200404_2007'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuosittuHaku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vuosi', models.IntegerField()),
                ('Kk', models.IntegerField()),
                ('Kunta', models.CharField(max_length=100)),
            ],
        ),
    ]
