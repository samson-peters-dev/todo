from django.urls import path
from . import views
urlpatterns = [
    path('create/',views.TodoCreateGetView.as_view()),
    path('retrieve/',views.TodoCreateGetView.as_view()),
    path('get/<str:id>/',views.TodoGetUpdateDeleteView.as_view()),
    path('update/<str:id>/',views.TodoGetUpdateDeleteView.as_view()),
    path('delete/<str:id>/',views.TodoGetUpdateDeleteView.as_view()),
]