from django.db import models


# Create your models here.

class Food(models.Model):
    price = models.FloatField(verbose_name='Цена', default=None)
    brand = models.CharField(verbose_name='Бренд', default='', max_length=255)
    description = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(verbose_name='Дата выпуска')

    def __str__(self):
        return '{} {} {} {}'.format(self.brand, self.date, self.price, self.description)

    class Meta:
        verbose_name = 'Еда'
        verbose_name_plural = 'Еда'
