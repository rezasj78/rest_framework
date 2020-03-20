import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .utils import jwt_response_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_response_payload_handler = jwt_response_payload_handler
expire_delta = api_settings.JWT_REFRESH_EXPIRATION_DELTA


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    token = serializers.SerializerMethodField(read_only=True)
    expires = serializers.SerializerMethodField(read_only=True)
    token_response = serializers.SerializerMethodField(read_only=True)
    addr = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2',
            'token',
            'expires',
            'addr'
            # 'token_response'
        ]
        extra_kwargs = {'password': {'write_only': True}}

    def get_request(self):  # TODO in case request is needed (it's passed in views)
        context = self.context
        request = context['request']

    def get_token_response(self, obj):  # TODO use this OR get_token
        context = self.context
        request = context['request']
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return jwt_response_payload_handler(user=obj, token=token, request=request)

    def get_addr(self, obj):
        context = self.context
        request = context['request']
        ip_addr = request.META['REMOTE_ADDR']
        return ip_addr


    def validate_email(self, value):
        print(value)
        if value is None or value == '':
            return value
        user = User.objects.filter(email__iexact=value)
        if user.exists():
            raise serializers.ValidationError('user with this email already exits')
        return value

    def validate_usernamel(self, value):
        user = User.objects.filter(username__iexact=value)
        if user.exists():
            raise serializers.ValidationError('user with this username already exits')
        return value

    def get_token(self, obj):
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def get_expires(self, obj):
        return timezone.now() + expire_delta - datetime.timedelta(seconds=200)

    def validate(self, data):
        pw = data.get('password')
        pw2 = data.get('password2')  # TODO can be popped and not needing to override create method
        if pw != pw2:
            raise serializers.ValidationError('Password must match')
        return data

    def create(self, validated_data):
        user = User.objects.create_user(validated_data.get('username'), validated_data.get('email'),
                                        validated_data.get('password'))
        user.save()
        user.is_active = False
        return user
