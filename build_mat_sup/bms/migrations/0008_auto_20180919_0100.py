# Generated by Django 2.1.1 on 2018-09-18 19:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0007_auto_20180917_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='vr_no',
            field=models.CharField(blank=True, default=uuid.uuid4, editable=False, max_length=15, primary_key=True, serialize=False),
        ),
    ]
