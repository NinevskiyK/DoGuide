# Generated by Django 2.2.4 on 2020-04-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20200413_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='excursion',
            name='Number_of_user',
            field=models.SmallIntegerField(default=0, help_text='Сколько человек записалось на твою экскурсию'),
        ),
    ]