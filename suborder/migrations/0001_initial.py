# Generated by Django 2.2 on 2019-04-16 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suborder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(max_length=2)),
                ('is_returned', models.BooleanField()),
                ('order_date', models.DateField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.Book')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]