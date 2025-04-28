from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
    path('properties/book/<int:property_id>/', views.book_property, name='book_property'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
]