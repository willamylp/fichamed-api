from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.UserListCreateView.as_view(), name='users-list-create'),
    path('user/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user-datail-view'),
]
