
from django.urls import path

from todo import views


urlpatterns = [
    path('category',views.category.index),
    path('category/<id>',views.category.detail),
]
