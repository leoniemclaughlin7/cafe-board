from . import views
from django.urls import path


urlpatterns = [
    path('', views.review, name='review'),
    path('menu/', views.menu, name='menu')
]
