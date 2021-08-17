from django.db import models
from Products.models import Category


class PhotosForOrder(models.Model):
    photo = models.ImageField(upload_to='photo_for_order/%Y/%m/%d')

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Фото на заказ'
        verbose_name_plural = 'Фотки на заказ'


class ToOrder(models.Model):
    TYPE_CHOICES = (
        ('Деревняний вироб', 'Деревняний вироб'),
        ('Писанка', 'Писанка'),
        ('Новорічні іграшка', 'Новорічні іграшка'),
    )
    MATERIAL_CHOICES = (
        ('Дерево', 'Дерево'),
        ('Пластик', 'Пластик'),
        ('Пінопласт', 'Пінопласт'),
    )

    SIZE_CHOICES = (
        ('Lg', 'Великий'),
        ('Md', 'Середній'),
        ('Sm', 'Маленький'),
    )

    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    material = models.CharField(max_length=30, choices=MATERIAL_CHOICES)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    description = models.TextField()
    telephone_number = models.CharField(max_length=12)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'На заказ'
        verbose_name_plural = 'На закази'
