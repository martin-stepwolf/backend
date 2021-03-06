""" User URLs """

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
from .views import users as users_views

# Django imports
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', users_views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
