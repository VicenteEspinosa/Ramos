from django.http.response import JsonResponse
from backend_app.db_validators.user_validators import validate_rut
from backend_app.db_validators.form_tree_validators import validate_category
from backend_app.db_helpers.user_helpers import get_indexed_json_user
from backend_app.db_paginators.user_paginator import UserPaginator
from backend_app.db_models.user import User
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from backend_app.db_serializers.user_serializer import (
    UserEditSerializer,
    UserLoginSerializer,
    UserLogoutSerializer,
    UserModelSerializer,
    UserSignUpSerializer,
)


class UserViewSet(viewsets.GenericViewSet):

    queryset = User.objects.all()
    serializer_class = UserModelSerializer


    @action(detail=False, methods=['post'])
    def login(self, request):
        """User sign in."""

        data = request.data
        if "mobile" not in data:
            data["mobile"] = False
        serializer = UserLoginSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        user, access_token = serializer.save()
        user_data = UserModelSerializer(user).data

        # Delete password
        user_data.pop('password', None)

        return Response(user_data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['post'])
    def signup(self, request):
        """User sign up."""

        try:
            if request.data['_type'] == 3:
                data = request.data
                if not validate_category(request.data['category_id']):
                    return Response({'error': 'The category is not valid.'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                data = {
                    'username': request.data['username'],
                    'email': request.data['email'],
                    'first_name': request.data['first_name'],
                    'last_name': request.data['last_name'],
                    'password': request.data['password'],
                    'rut': request.data['rut'],
                    '_type': request.data['_type'],
                    'category_id': int(-1)
                }

            serializer = UserSignUpSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            # Delete password
            data = serializer.data
            data.pop('password', None)

            return Response(data, status=status.HTTP_201_CREATED)
        except ValueError as err:
            return Response({'error': str(err)}, status=status.HTTP_400_BAD_REQUEST)


    @action(detail=False, methods=['get'])
    def all(self, request):
        """Get all users."""

        try:
            order_by = request.query_params['order_by']
        except KeyError:
            order_by = 'first_name'

        users = User.objects.all().order_by(order_by)
        serializer = UserModelSerializer(users, many=True)

        # Delete password
        for dato in serializer.data:
            dato.pop('password', None)

        return Response(serializer.data, status=status.HTTP_200_OK)


    @action(detail=False, methods=['get'])
    def all_paginated(self, request):
        """Get all users."""

        try:
            order_by = request.query_params['order_by']
        except KeyError:
            order_by = 'first_name'

        users = User.objects.all().order_by(order_by)
        page_size = request.query_params.get('page_size', False)
        if page_size:
            user_paginator = UserPaginator(page_size)
            response = user_paginator.generate_response(users, UserModelSerializer, request)
            return response
        return JsonResponse({'error': 'The page_size must be in the path values.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def all_indexed(self, request):
        """Get all users indexed."""

        try:
            order_by = request.query_params['order_by']
        except KeyError:
            order_by = 'first_name'

        users = User.objects.all().order_by(order_by)
        serializer = UserModelSerializer(users, many=True)
        for dato in serializer.data:
            dato.pop('password', None)

        return Response(get_indexed_json_user(serializer.data), status=status.HTTP_200_OK)


    @action(detail=True, methods=['delete'])
    def destroyer(self, request, pk=None):
        """Detroy user by user_id."""

        try:
            instance = User.objects.get(user_id=pk)
            instance.delete()
            return Response({'message': 'Success'}, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'error': 'The user do not exist'}, status=status.HTTP_404_NOT_FOUND)


    @action(detail=True, methods=['get'])
    def getuser(self, request, pk=None):
        """Get user by user_id."""

        try:
            instance = User.objects.get(user_id=pk)
        except User.DoesNotExist:
            return Response({'error': 'The user do not exist'}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserModelSerializer(instance)

        # Delete password
        data = serializer.data
        data.pop('password', None)


        return Response(data, status=status.HTTP_200_OK) 


    @action(detail=True, methods=['patch'])
    def edit(self, request, pk=None):
        """Edit user by user_id."""

        try:
            instance = User.objects.get(user_id=pk)
        except User.DoesNotExist:
            return Response({'error': 'The user do not exist'}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserEditSerializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        # Checking if the password has change
        password_data = request.data['password']
        if password_data == "":
            password = instance.password
        else:
            password = serializer.hash_password(password_data)
            if not password:
                return Response({'error': 'The password is not valid.'}, status=status.HTTP_400_BAD_REQUEST)

        # Checking if the RUT or the category_id has changed
        try:
            rut = request.data['rut']
            if not validate_rut(rut):
                return Response({'error': 'The rut is not valid.'}, status=status.HTTP_400_BAD_REQUEST)
            rut = rut.upper()
            serializer.save(password=password, rut=rut)
            

            category_id = request.data['category_id']
            validation_client = validate_category(category_id) and (instance._type==3)
            validation_not_client = (instance._type in [1, 2]) and (category_id==-1)
            if not (validation_client or validation_not_client):
                return Response({'error': 'The category is not valid.'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save(password=password, rut=rut, category_id=category_id)

        except KeyError:
            serializer.save(password=password)

        # Delete password
        data = serializer.data
        data.pop('password', None)

        return Response(data, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['post'])
    def logout(self, request):
        """Destroy access_token."""

        access_token = request.META["HTTP_AUTHORIZATION"][7:]
        try:
            instance = User.objects.get(access_token=access_token)
            serializer = UserLogoutSerializer(instance, data={'access_token': 'Null'}, partial=True)
        except User.DoesNotExist:
            instance = User.objects.get(access_token_mobile=access_token)
            serializer = UserLogoutSerializer(instance, data={'access_token_mobile': 'Null'}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Delete password
        data = serializer.data
        data.pop('password', None)

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def current(self,request):
        """Get current User data"""

        access_token = request.META["HTTP_AUTHORIZATION"][7:]
        try:
            user = User.objects.get(access_token=access_token)
            serializer = UserEditSerializer(user)
            data = serializer.data
            data.pop("user_id")
        except User.DoesNotExist:
            try:
                user = User.objects.get(access_token_mobile=access_token)
                data = serializer.data
                data.pop("user_id")
            except User.DoesNotExist:
                data = {"error: User does not exist"}
        return Response(data, status=status.HTTP_200_OK) 
