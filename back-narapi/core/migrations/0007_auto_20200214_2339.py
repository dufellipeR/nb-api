# Generated by Django 3.0.3 on 2020-02-14 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_character_baseoverall'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='baseoverall',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=155, null=True),
        ),
    ]
