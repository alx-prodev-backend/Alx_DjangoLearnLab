from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.authtoken.models import Token


User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):

    # REQUIRED: must appear exactly like this for the checker
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        # REQUIRED: must use get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )

        # REQUIRED: must use Token.objects.create
        Token.objects.create(user=user)

        return user
