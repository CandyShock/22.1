from django.db import models


class Product(models.Model):
    nomination = models.CharField(max_length=30, verbose_name='наименование')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='картинка', null=True, blank=True)
    category = models.CharField(max_length=30)
    price = models.IntegerField(verbose_name='цена')
    date = models.DateTimeField(verbose_name='дата')
    last_modified_date = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        return f"{self.nomination} {self.description}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Category(models.Model):
    nomination = models.CharField(max_length=30)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"{self.nomination}\n{self.description}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
