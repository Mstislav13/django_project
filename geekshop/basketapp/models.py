from django.db import models

from geekshop import settings
from mainapp.models import Product


class Basket(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='basket',
        verbose_name='пользователь',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='товар',
    )
    quantity = models.PositiveIntegerField(
        verbose_name='количество',
        default=0,
    )
    add_datetime = models.DateTimeField(
        verbose_name='время',
        auto_now_add=True,
    )

    def __str__(self):
         return f"Товар в корзине - {self.pk}"

    class Meta:
         verbose_name = 'корзина'
         verbose_name_plural = 'товар в корзине'
