from django.urls import path

from . import views

app_name = 'generate'

urlpatterns = [
    path('', views.generate, name='generate'),
]
