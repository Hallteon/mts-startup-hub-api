from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer, UserSerializer


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('email', 'firstname', 'lastname', 'password')
