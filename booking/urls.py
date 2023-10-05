from . import views
from django.urls import path


urlpatterns = [
    path('booking', views.customer_booking, name='booking'),
    path('display_booking', views.display_booking, name='display_booking')

]
