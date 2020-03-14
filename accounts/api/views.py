from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.models import User
from django.db.models import Q
from rest_framework_jwt.settings import api_settings
from .utils import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = jwt_response_payload_handler


class AuthView(APIView):
    permission_classes = [AllowAny]
    http_method_names = ['post', 'get', 'options']

    def get(self, request, *args, **kwargs):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        qs = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).distinct()
        print(qs)
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            print("Auth")
            return Response({'message': 'already Authenticated'})
        else:
            print("not")
        return Response({'message': 'Use this endpoint for creating Auth tokens'})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("Auth")
            return Response({'message': 'already authenticated'})
        data = request.data
        username = data.get('username')
        password = data.get('password')
        qs = User.objects.filter(
            Q(username__iexact=username) or Q(email__iexact=username)
        )
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                payload = jwt_payload_handler(user_obj)
                token = jwt_encode_handler(payload)
                return Response({'token': token, 'user': user_obj.username})
        # user = authenticate(username=username, password=password)
        return Response({'message': 'Invalid Credentials'})
