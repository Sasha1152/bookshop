# Generated by Django 2.2 on 2020-01-30 16:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('image', '0001_initial'),
        ('genre', '0001_initial'),
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('year', models.PositiveSmallIntegerField(blank=True, max_length=4, null=True)),
                ('pages', models.PositiveSmallIntegerField(blank=True, max_length=5, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('quantity', models.PositiveSmallIntegerField(default=1, max_length=2, null=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='author.Author')),
                ('genre', models.ManyToManyField(blank=True, null=True, related_name='genre', to='genre.Genre')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='image.Image')),
            ],
        ),
    ]
