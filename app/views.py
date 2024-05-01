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
            'Patient': {
                'patient_list_create': reverse('patient_list_create', request=request, format=format),
                'patient_datail_view/<int:pk>': reverse('patient_datail_view', kwargs={'pk': 1}, request=request, format=format),
            },
        })
