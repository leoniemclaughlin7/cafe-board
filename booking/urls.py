from booking.views import get_home_page
from django.urls import path


urlpatterns = [
    path('', get_home_page, name='home'),
]
