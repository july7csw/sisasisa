from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import UserRegistrationView, UserLoginView, SocialLoginCallbackView
import user.views as views

urlpatterns = [
    path('user/create/', UserRegistrationView.as_view()),
    path('user/login/', UserLoginView.as_view()),
    path('user/logout/', LogoutView.as_view()),
    path('user/login/social/<provider>/callback/', SocialLoginCallbackView.as_view()),
]
