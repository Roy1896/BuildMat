# Generated by Django 2.1.1 on 2018-09-19 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0010_auto_20180919_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='vr_no',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
    ]
