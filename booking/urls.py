from . import views
from django.urls import path


urlpatterns = [
    path('booking', views.customer_booking, name='booking'),
    path('display_booking', views.display_booking, name='display_booking'),
    path('edit_booking/<booking_id>/<customer_id>',
         views.edit_booking, name='edit_booking'),
    path('delete_booking/<booking_id>/<customer_id>',
         views.delete_booking, name='delete_booking'),

]
