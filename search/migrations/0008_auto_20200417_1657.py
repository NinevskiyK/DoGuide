# Generated by Django 2.2.4 on 2020-04-17 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0007_auto_20200417_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursion',
            name='Made_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lk.Profile'),
        ),
    ]
