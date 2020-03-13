from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate, get_user_model


class AuthView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            print("Auth")
        else:
            print("not")
        return Response({'message': 'Worked'})

    def post(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            print("Auth")
            return Response('')
        data = request.data
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        return Response({'name': user})
