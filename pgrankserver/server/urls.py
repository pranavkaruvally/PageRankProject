from django.urls import path
from . import views

urlpatterns = [
     path('', views.home),
     path('result', views.result),
     path('update', views.update_view),
     path('api/update', views.update_api),
]
