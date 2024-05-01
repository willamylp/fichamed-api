from django.urls import path
from . import views


urlpatterns = [
    path('medical_history/', views.MedicalCareHistoryListCreateView.as_view(), name='medical_history_list_create'),
    path('medical_history/<int:pk>/', views.MedicalCareHistoryRetrieveDestroyView.as_view(), name='medical_history_datail_view'),
]
