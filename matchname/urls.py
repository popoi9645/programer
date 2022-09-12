from django.urls import path

from matchname import views

urlpatterns = [
    path('solupath/', views.home),
]