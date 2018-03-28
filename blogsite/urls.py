from django.urls import path
from . import views

urlpatterns = [
	path('$/', views.post, name='posts'),
	path('$/', views.comments, name='comments'),
]