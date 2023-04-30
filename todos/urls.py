from django.urls import path
from todos import views

urlpatterns = [
    path('', views.ToDoView.as_view(), name='todo_view'),
    path('<int:todo_id>/', views.ToDoDetailView.as_view(), name='tododetail_view'),
    path('<int:todo_id>/complete/', views.ToDoCompleteView.as_view(), name='todocomplete_view')
]