from django.utils import timezone

from django.db import models

# 10) СОЗДАНИЕ МОДЕЛЕЙ

# Создание модели "категории курсов обучения" в каждой записи которой есть два поля
class Category(models.Model):
    title = models.CharField(max_length=255) # значение в виде строки с максимальной длинной строки 255
    created_at = models.DateTimeField(default=timezone.now) # дата автоматически генерируется с текущей датой

# Создание модели "курсы обучения в составе категории"
class Curse(models.Model):
    title = models.CharField(max_length=255)

    price = models.FloatField() # цена = число с плавающей точкой
    students_qty = models.IntegerField() # количество студентов = целое число
    reviews_qty = models.IntegerField() # количество отзывов = целое число
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # категория = ключ из другой таблицы (Категория,
                                                                      # при удалении которой удаляются все курсы).
    created_at = models.DateTimeField(default=timezone.now)











