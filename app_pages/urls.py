from django.urls import path
from .views import index, about


urlpatterns = [
    path('about/', index, name='index'),
    path('', index, name='index'),
]