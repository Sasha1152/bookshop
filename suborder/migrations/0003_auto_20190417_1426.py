# Generated by Django 2.2 on 2019-04-17 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suborder', '0002_auto_20190417_1127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suborder',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
