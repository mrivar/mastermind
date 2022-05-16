from django.urls import path
from game import views

urlpatterns = [
    path('game/', views.GameList.as_view()),
    path('game/<int:pk>', views.GameDetail.as_view()),
]
