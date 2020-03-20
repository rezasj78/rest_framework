from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate, get_user_model, login
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework_jwt.settings import api_settings
from .utils import jwt_response_payload_handler
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import UserRegisterSerializer

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = jwt_response_payload_handler


class AuthView(APIView):
    authentication_classes = [JSONWebTokenAuthentication]
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
        return Response({'message': 'Use this endpoint for creating Auth tokens', 'ip_address': request.META['REMOTE_ADDR']})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print("Auth")
            return Response({'message': 'already authenticated'})
        data = request.data
        username = data.get('username')
        password = data.get('password')
        qs = User.objects.filter(
            Q(username__iexact=username) | Q(email__iexact=username)).distinct()
        if qs.count() == 1:
            user_obj = qs.first()
            if user_obj.check_password(password):
                payload = jwt_payload_handler(user_obj)
                token = jwt_encode_handler(payload)
                return Response({'token': token, 'user': user_obj.username})
        # user = authenticate(username=username, password=password)
        return Response({'message': 'Invalid Credentials'}, status=401)


class RegisterView(CreateAPIView):  # TODO With Serializer
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_context(self, *args, **kwargs): # TODO how to pass anything to serializer
        return {'request': self.request}
# class RegisterView(APIView): # TODO NOT With Serializer
#     authentication_classes = [JSONWebTokenAuthentication]
#     permission_classes = [AllowAny]
#     http_method_names = ['post', 'get', 'options']
#
#     def get(self, request, *args, **kwargs):
#         data = request.data
#         username = data.get('username')
#         password = data.get('password')
#         email = data.get('email')
#         qs = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=email))
#         print(qs.first())
#         print(request.user.is_authenticated)
#         if request.user.is_authenticated:
#             print("Auth")
#             return Response({'message': 'already registered and Authenticated'})
#         else:
#             print("not")
#         return Response({'message': 'Use this endpoint for Registering and creating Auth tokens'})
#
#     def post(self, request, *args, **kwargs):
#         if request.user.is_authenticated:
#             print("Auth")
#             return Response({'message': 'already registered and Authenticated'})
#         data = request.data
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#         password2 = data.get('password2')
#         if password != password2:
#             return Response({'message': 'password do not match'}, status=401)
#         qs = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=email))
#         if qs.exists():
#             return Response({'message': 'user already exits'}, status=401)
#         else:
#             user = User.objects.create_user(username=username, email=email, password=password)
#             user.save()
#             payload = jwt_payload_handler(user)
#             token = jwt_encode_handler(payload)
#             return Response({'message': 'user created', 'token': token, 'user': user.username, 'email': user.email},
#                             status=201)
#         # return Response({'message': 'Invalid Credentials'}, status=401)
