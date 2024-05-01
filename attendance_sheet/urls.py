from django.urls import path
from . import views


urlpatterns = [
    path('attendance_sheet/', views.AttendanceSheetListCreateView.as_view(), name='attendance_sheet_list_create'),
    path('attendance_sheet/<int:pk>/', views.AttendanceSheetRetrieveUpdateDestroyView.as_view(), name='attendance_sheet_datail_view'),
]
