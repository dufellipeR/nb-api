# Generated by Django 3.0.3 on 2020-02-14 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200208_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='bonus',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=155, null=True),
        ),
        migrations.AddField(
            model_name='character',
            name='overall',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=155, null=True),
        ),
    ]
