from django.urls import path
from . import views


urlpatterns = [
    path('patient/', views.PatientListCreateView.as_view(), name='patient_list_create'),
    path('patient/<int:pk>/', views.PatientRetrieveUpdateDestroyView.as_view(), name='patient_datail_view'),
]
