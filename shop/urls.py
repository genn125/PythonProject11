from django.urls import path

from base.urls import urlpatterns
from  . import views

urlpatterns = [path('',views.index, name='index')]