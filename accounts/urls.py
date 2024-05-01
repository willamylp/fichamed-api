from django.urls import path
from . import views

urlpatterns = [
    path('user/', views.UserListCreateView.as_view(), name='users_list_create'),
    path('user/<int:pk>/', views.UserRetrieveUpdateDestroyView.as_view(), name='user_datail_view'),
]
