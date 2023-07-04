from django.db import models
from django.urls import reverse


class Products(models.Model):
    title = models.CharField(max_length=80)
    slug = models.SlugField(max_length=150, verbose_name='Url', unique=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default='default', null=True)
    price = models.SmallIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    descriptions = models.TextField(blank=True)
    photos = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=False)
    views = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('show_by_name', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'


class Category(models.Model):
    title = models.CharField(max_length=80, db_index=True)
    slug = models.SlugField(max_length=150, verbose_name='Url', unique=True)

    class Meta:
        verbose_name = 'Катугорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return self.title


class Images(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d')

    class Meta:
        verbose_name = 'Фотографія'
        verbose_name_plural = 'Фотографії'

    def __str__(self):
        return str(self.pk)


class ImagesForSlider(Images):
    in_slider = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Фотографія для слайдера'
        verbose_name_plural = 'Фотографії для слайдера'


class Collection(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=170, null=True, unique=True)
    products = models.ManyToManyField('Products', related_name='collection')
    photos = models.ManyToManyField('Images', related_name='collection')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_published = models.BooleanField(default=False)
    views = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = 'Колекція'
        verbose_name_plural = 'Колекції'

    def __str__(self):
        return self.title
