from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.APIRootView.as_view(), name='api_root'),
    path('api/v1/', views.APIRootView.as_view(), name='api_root'),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('accounts.urls')),
    path('api/v1/', include('attendance_sheet.urls')),
    path('api/v1/', include('medical_history.urls')),
]
