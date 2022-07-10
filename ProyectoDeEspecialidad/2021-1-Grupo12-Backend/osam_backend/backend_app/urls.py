from backend_app.db_views import user_view
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', user_view.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls))
]
