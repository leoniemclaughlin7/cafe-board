from . import views
from django.urls import path


urlpatterns = [
    path('booking', views.customer_booking, name='booking'),
    
]
