from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz, name='quiz'),
    path('check-answer/', views.check_answer, name='check_answer'),
] 