from django.urls import path
from .views import home_view, about

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', about, name='about'),
]
