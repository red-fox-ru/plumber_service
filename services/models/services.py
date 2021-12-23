from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя категории', blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class ObjectRepair(models.Model):
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование', blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Service(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(ObjectRepair, verbose_name='Категория', on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Наименование', blank=True)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='product_image', blank=True, verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание', null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    location = models.TextField(blank=True, verbose_name='Локация', null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_start = models.DateTimeField(auto_now_add=False)
    date_end = models.DateTimeField(auto_now_add=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
