from django.contrib import admin
# 20) Регистрируем модели, которые создали для приложения shop
from . import models

admin.site.register(models.Course)
admin.site.register(models.Category)
# Register your models here.
