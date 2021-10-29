#!/usr/bin/env python
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from store.serializers import Text, TextSerializer
# Create your views here.

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def read_text(request, hash):
    text = get_object_or_404(Text, hash=hash)
    text_value = text.value
    text.delete()

    return Response(data={"text": text_value})

class UserTextViewSet(ModelViewSet):

    serializer_class = TextSerializer
    queryset = Text.objects.all()
    permission_classes = [IsAuthenticated]

    def filter_queryset(self, queryset):
        queryset = self.request.user.texts.all()

        return super().filter_queryset(queryset)

    def update(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        
        return super().update(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        request.data["user"] = request.user.id
        
        return super().create(request, *args, **kwargs)