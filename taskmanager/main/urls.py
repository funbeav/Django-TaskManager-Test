from django.urls import path
from . import views


app_name = 'task'
urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('create/', views.create, name='create'),
    path('<int:task_id>/edit/', views.edit, name='edit'),
    path('<int:task_id>/delete/', views.delete, name='delete')
]