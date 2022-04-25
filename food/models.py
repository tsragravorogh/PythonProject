from django.db import models
from django.db.models import SET_NULL


# Create your models here.
class Country(models.Model):
    name = models.CharField('Страна', max_length=256)

    def __str__(self):
        return '{}'.format(self.name)


class Brand(models.Model):
    name = models.CharField('Бренд', max_length=256)
    country = models.ForeignKey(Country, on_delete=SET_NULL, null=True, blank=True)
    city = models.CharField(verbose_name='Город производства', max_length=255, default='')

    def __str__(self):
        return '{}'.format(self.name)


class TypeFood(models.Model):
    name = models.CharField('Тип продукции', max_length=256)

    def __str__(self):
        return '{}'.format(self.name)

# еда - тип прод, бренд,


class Food(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256, default='')
    price = models.IntegerField(verbose_name='Цена', default=0)
    brand = models.ForeignKey(Brand, on_delete=SET_NULL, null=True, blank=True)
    description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Дата выпуска')
    weight = models.IntegerField(verbose_name='Масса нетто')
    type = models.ForeignKey(TypeFood, on_delete=SET_NULL, null=True, blank=True)
    image = models.ImageField(null=True, verbose_name='Изображение', blank=True)

    def __str__(self):
        return '{} {} {} {} {}'.format(self.name, self.brand, self.date, self.price, self.description)

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'
