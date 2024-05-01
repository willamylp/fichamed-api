from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


class APIRootView(APIView):

    def get(self, request, format=None):
        return Response({
            'Authentication': {
                'token_obtain_pair': reverse('token_obtain_pair', request=request, format=format),
                'token_refresh': reverse('token_refresh', request=request, format=format),
                'token_verify': reverse('token_verify', request=request, format=format),
            },
            'Accounts': {
                'users_list_create': reverse('users_list_create', request=request, format=format),
                'user_datail_view/<int:pk>': reverse('user_datail_view', kwargs={'pk': 1}, request=request, format=format),
            },
            'AttendanceSheet': {
                'attendance_sheet_list_create': reverse('attendance_sheet_list_create', request=request, format=format),
                'attendance_sheet_datail_view/<int:pk>': reverse('attendance_sheet_datail_view', kwargs={'pk': 1}, request=request, format=format),
                'attendance_sheet_panel_list': reverse('attendance_sheet_panel_list', request=request, format=format),
            },
            'MedicalCareHistory': {
                'medical_history_list_create': reverse('medical_history_list_create', request=request, format=format),
                'medical_history_datail_view/<int:pk>': reverse('medical_history_datail_view', kwargs={'pk': 1}, request=request, format=format),
            },
        })
