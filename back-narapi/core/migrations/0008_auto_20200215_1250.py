# Generated by Django 3.0.3 on 2020-02-15 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20200214_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='baseoverall',
            field=models.IntegerField(blank=True, max_length=155, null=True),
        ),
    ]