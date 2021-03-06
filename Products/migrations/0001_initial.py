# Generated by Django 3.2.4 on 2021-07-06 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=80)),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Url')),
            ],
            options={
                'verbose_name': 'Катугорія',
                'verbose_name_plural': 'Категорії',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('price', models.SmallIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('descriptions', models.TextField(blank=True)),
                ('photos', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('is_published', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='Url')),
                ('category', models.ForeignKey(default='default', null=True, on_delete=django.db.models.deletion.PROTECT, to='Products.category')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товари',
            },
        ),
    ]
