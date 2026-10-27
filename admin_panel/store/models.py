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