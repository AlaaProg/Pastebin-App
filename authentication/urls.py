
from django.urls import path
from authentication.views import RegisterView, get_current_user
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [

    path('login/', TokenObtainPairView.as_view(), name='login_user'),
    path('register/', RegisterView.as_view(), name='create_new_user'),
    path('me/', get_current_user, name='current_user'),

]

    