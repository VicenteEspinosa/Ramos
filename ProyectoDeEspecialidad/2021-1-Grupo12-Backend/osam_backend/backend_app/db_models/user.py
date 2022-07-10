from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from djongo import models
from backend_app.db_validators.user_validators import validate_rut
from django.core.validators import MaxValueValidator, MinValueValidator


class OsamManager(BaseUserManager):
    """The OSAM Manager."""

    def create_user(self, username, email, first_name, last_name, password, rut, _type, category_id):
        """Creates and saves a User with the data given."""
        
        if User.objects.all().count() > 0:
            user_id = list(User.objects.all().order_by('-user_id'))[0].user_id + 1
        else:
            user_id = 0

        # Verifiying email
        exist_email = User.objects.filter(email=email).exists()
        if not email:
            raise ValueError('Users must have an email address.')
        if exist_email:
            raise ValueError('The email address is already been used.')

        # Verify RUT
        if not validate_rut(rut):
            raise ValueError('The RUT is not valid.')
        rut = rut.upper()
        exist_rut = User.objects.filter(rut=rut).exists()
        if exist_rut:
            raise ValueError('The RUT is already been used.')

        user = self.model(
            user_id=user_id,
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
            rut=rut,
            _type=_type,
            category_id=category_id
        )

        user.save(using=self._db)
        return user


class User(AbstractBaseUser, models.Model):
    """The OSAM user model."""

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    rut = models.CharField(max_length=10, unique=True)
    _type = models.IntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)])
    access_token = models.CharField(max_length=255, default='Null', blank=True)
    access_token_mobile = models.CharField(max_length=255, default='Null', blank=True)
    last_login = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True)
    category_id = models.IntegerField()
    fields = '__all__'
    objects = OsamManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] # type: ignore
