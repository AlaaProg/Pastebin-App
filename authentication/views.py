from django.contrib.auth.models import User
from rest_framework import response, decorators, permissions
from authentication.serializers import RegisterSerializer
from rest_framework import generics

@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAuthenticated])
def get_current_user(request):
    
    serializer = RegisterSerializer(request.user)
    return response.Response(serializer.data)

class RegisterView(generics.CreateAPIView):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer