from django.urls import path
from accounts.api.v1.views import * 
from rest_framework_simplejwt.views import (TokenRefreshView, TokenVerifyView)


urlpatterns = [

    # registration
    path('registration/',RegistrationApiView.as_view(), name='registration' ),
    # login token
    path('token/login/', CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', CustomDiscardAuthToken.as_view(), name='token-logout'),
    # login JWT
    path('jwt/create/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('jwt/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # change password
    path('change-password/', ChangePasswordApiView.as_view(), name='change-password'),
    # activation
    
    #resend activation

    path('send-email/' ,EmailSend.as_view(), name='send-email')
    
]