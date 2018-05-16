from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello, name='hello'),
    path('board/', views.note, name='note'),
    path('write/', views.Write.as_view(), name='write'),
]