from django.urls import path
from . import views

urlpatterns = [
    path('animals/', views.AnimalView.as_view()),
    path('animals/<int:animal_id>', views.SingleAnimalView.as_view())
]