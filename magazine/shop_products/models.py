from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=50, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=50, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    text = models.TextField(verbose_name="Описание продукта", max_length=200, db_index=True)
    time = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


