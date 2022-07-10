from datetime import datetime

from backend_app.db_models.user import User
import bcrypt
from django.contrib.auth import password_validation
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class UserModelSerializer(serializers.ModelSerializer):
    """User serizalizer."""

    class Meta:
        """Meta."""

        model = User
        fields = '__all__'


class UserEditSerializer(serializers.ModelSerializer):
    """User edit serizalizer."""

    class Meta:
        """Meta."""

        _type = serializers.IntegerField(min_value=1, max_value=3)

        model = User
        fields = (
            'user_id',
            'username',
            'email',
            'first_name',
            'last_name',
            'rut',
            '_type',
            'category_id',
        )

    def hash_password(self, password):
        """Change to hash password and checking the length."""

        if (len(password) >= 8):
            password = make_password(password)
            return password
        return False


class UserLogoutSerializer(serializers.ModelSerializer):
    """User logout serizalizer."""

    access_token = serializers.CharField()
    access_token_mobile = serializers.CharField()

    class Meta:
        """Meta."""

        model = User
        fields = (
            'access_token',
            'access_token_mobile'
        )


class UserLoginSerializer(serializers.Serializer):
    """User login serizalizer."""

    username = serializers.CharField()
    password = serializers.CharField(min_length=8, max_length=64)
    mobile = serializers.BooleanField()

    def validate(self, data):
        """Validate."""

        users = User.objects.filter(username=data['username'])
        for user in users:
            user_valid = user.check_password(data['password'])
            if user_valid:
                self.context['user'] = user
                return data
        raise serializers.ValidationError('Las credenciales no son válidas')

    def create(self, data):
        """Generar o recuperar access_token."""

        salt = bcrypt.gensalt()
        access_token = bcrypt.hashpw(data['username'].encode('utf-8'), salt)

        self.context['user'].last_login = datetime.now()
        if not data["mobile"]:
            self.context['user'].access_token = access_token
        else:
            self.context['user'].access_token_mobile = access_token
        self.context['user'].password = make_password(data['password'])
        self.context['user'].save()

        return self.context['user'], access_token


class UserSignUpSerializer(serializers.Serializer):
    """User singup serizalizer."""

    email = serializers.EmailField()
    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, max_length=64)
    first_name = serializers.CharField(min_length=2, max_length=50)
    last_name = serializers.CharField(min_length=2, max_length=100)
    rut = serializers.CharField(min_length=9, max_length=10)
    _type = serializers.IntegerField(min_value=1, max_value=3)
    category_id = serializers.IntegerField()

    def validate(self, data):
        """Validate."""

        passwd = data['password']
        password_validation.validate_password(passwd)
        return data

    def create(self, data):
        """Create."""

        data['password'] = make_password(data['password'])
        user = User.objects.create_user(**data)
        return user


class UserGetAllSerializer(serializers.Serializer):
    """User GET all serizalizer."""

    def validate(self, data):
        """validate."""

        valid = True
        if not valid:
            raise serializers.ValidationError('Las credenciales no son válidas')

        return data

    def create(self, data):
        """Generar o recuperar access_token."""

        return self.context['user']
