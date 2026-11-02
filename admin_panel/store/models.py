from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    telegram = models.BigIntegerField(unique=True)
    phone = models.CharField(max_length=20, null=True, blank=True)

    class Meta:
        db_table = 'users'
        managed = False
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']

    def __str__(self):
        return self.name


class Categories(models.Model):
    category_name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 'categories'
        managed = False
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Products(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.PROTECT, related_name='products')
    product_name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products'
        managed = False
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['id']

    def __str__(self):
        return self.product_name


class Orders(models.Model):
    product_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    final_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'orders'
        managed = False
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.product_name} x{self.quantity} — {self.final_price} руб"
