
from django.urls import path

from todo import views


urlpatterns = [
    path('category',views.category.index),
    path('category/<id>',views.category.detail),
    path('todo', views.todo.TodoList.as_view()),
    path('todo/<id>', views.todo.TodoDetail.as_view()),
    
]
