from rest_framework import serializers

from django.contrib.auth import get_user_model

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField(required=False)
    phone_number = serializers.CharField(required=False)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if not phone_number:
            raise serializers.ValidationError("Telefon raqam kiriting!")

        user = User.objects.filter(phone_number=phone_number).first()

        if not user:
            raise serializers.ValidationError("Foydalanuvchi topilmadi!")

        if not user.check_password(password):
            raise serializers.ValidationError("Parol noto'g'ri")

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
