from django.urls import path, include
from accounts.api.v1.views import * 
#from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import (TokenRefreshView, TokenVerifyView)


app_name = 'api-v1'

urlpatterns = [

    # registration
    path('registration/',RegistrationApiView.as_view(), name='registration' ),
    path('token/login/', CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiscardAuthToken.as_view(), name='token-logout'),

    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('change-password/', ChangePasswordApiView.as_view(), name='change-password'),

    path('profile/', ProfileApiView.as_view(), name='profile'),
]