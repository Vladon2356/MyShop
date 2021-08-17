# Generated by Django 3.2.4 on 2021-08-16 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotosForOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photo_for_order/%Y/%m/%d')),
            ],
            options={
                'verbose_name': 'Фото на заказ',
                'verbose_name_plural': 'Фотки на заказ',
            },
        ),
        migrations.CreateModel(
            name='ToOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Деревняний вироб', 'Деревняний вироб'), ('Писанка', 'Писанка'), ('Новорічні іграшка', 'Новорічні іграшка')], max_length=30)),
                ('material', models.CharField(choices=[('Дерево', 'Дерево'), ('Пластик', 'Пластик'), ('Пінопласт', 'Пінопласт')], max_length=30)),
                ('size', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('telephone_number', models.CharField(max_length=12)),
            ],
            options={
                'verbose_name': 'На заказ',
                'verbose_name_plural': 'На закази',
            },
        ),
    ]
