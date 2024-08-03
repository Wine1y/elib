from django.urls import path
from rest_framework_simplejwt.views import (
                                            TokenObtainPairView, TokenRefreshView,
                                            TokenBlacklistView
                                           )


app_name = "auth"
urlpatterns = [
    path('jwt/create', TokenObtainPairView.as_view(), name="auth_create"),
    path('jwt/refresh', TokenRefreshView.as_view(), name="auth_refresh"),
    path('jwt/blacklist', TokenBlacklistView.as_view(), name="auth_blacklist")
]