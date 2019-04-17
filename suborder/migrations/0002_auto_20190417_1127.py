# Generated by Django 2.2 on 2019-04-17 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('suborder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suborder',
            name='book_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.Book'),
        ),
        migrations.AlterField(
            model_name='suborder',
            name='order_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='order.Order'),
        ),
    ]
