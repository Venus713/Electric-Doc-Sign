from django.contrib.auth import get_user_model
from rest_framework.serializers import BooleanField
from rest_auth.serializers import UserDetailsSerializer
from rest_auth.registration.serializers import RegisterSerializer


class DocSignUserDetailSerializer(UserDetailsSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            'pk', 'username', 'email', 'first_name', 'last_name',
            'is_superuser', 'items_in_cart')
        read_only_fields = ('email', 'is_superuser')


class DocSignRegisterSerializer(RegisterSerializer):
    
    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', '')
        }
