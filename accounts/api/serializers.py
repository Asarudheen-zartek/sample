from rest_framework import serializers
from ..models import User

from django.contrib.auth import authenticate, get_user_model
from rest_framework.exceptions import AuthenticationFailed

class  UserSerializer(serializers.ModelSerializer):

    birthday = serializers.BooleanField(source='is_birthday', read_only=True)
    auth_tokens = serializers.JSONField(source='tokens', read_only=True)


    class Meta:
        model =  User
        fields = (
            'email',
            'name',
            'date_of_birth',
            'birthday',
            'auth_tokens',
        )



class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(
        max_length=68, min_length=3, write_only=True)

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model =  User
        fields = (
            'email',
            'password',
            'tokens',
        )

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
    
        user = authenticate(**attrs)
                
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again!')
   
        return super().validate(attrs)