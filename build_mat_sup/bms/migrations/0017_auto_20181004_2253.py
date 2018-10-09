# Generated by Django 2.1.1 on 2018-10-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0016_auto_20181004_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='businesspartnermaster',
            name='bp_type',
            field=models.CharField(choices=[('Buyer', 'Buyer'), ('Supplier', 'Supplier')], default='none', max_length=10, verbose_name='Business Partner Type'),
        ),
    ]
