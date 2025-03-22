from django.utils import timezone    # для создания =timezone.now

from django.db import models

# 10) СОЗДАНИЕ МОДЕЛЕЙ

# Создание модели "категории курсов обучения" в каждой записи которой есть два поля
class Category(models.Model):
    title = models.CharField(max_length=255) # значение в виде строки с максимальной длинной строки 255
    created_at = models.DateTimeField(default=timezone.now) # дата автоматически генерируется с текущей датой

# 21а) Добавление магического метода для изменения названия таблиц на сайте в админ панели

    def __str__(self):    # конвертация Category object (1) на сайте в название курса по удобочитаемо
        return self.title


# Создание модели "курсы обучения в составе категории"
class Course(models.Model):
    title = models.CharField(max_length=300)
    price = models.FloatField() # цена = число с плавающей точкой
    students_qty = models.IntegerField() # количество студентов = целое число
    reviews_qty = models.IntegerField() # количество отзывов = целое число
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # категория = ключ из другой таблицы (Категория,
                                                                    # при удалении которой удаляются все курсы).
    created_at = models.DateTimeField(default=timezone.now)

    # 21в) Добавление магического метода для изменения названия таблиц на сайте в админ панели
    def __str__(self):    # конвертация Curse object на сайте в название курса удобочитаемо
        return self.title + ' ' + str(self.students_qty) + ' ' + 'человек'  # Можно использовать и f-строку









