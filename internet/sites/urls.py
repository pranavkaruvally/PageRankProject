from django.urls import path
from . import views

urlpatterns = [
    path('health/<str:site_id>', views.health_view, name='health'),
    path('technology/<str:site_id>', views.technology_view, name='health'),
    path('cars/<str:site_id>', views.cars_view, name='health'),
    path('animals/<str:site_id>', views.animals_view, name='health'),
    path('business/<str:site_id>', views.business_view, name='health'),
    path('movies/<str:site_id>', views.movies_view, name='health'),
]
