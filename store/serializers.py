import secrets
from django.conf import settings
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, StringRelatedField
from store.models import Text, User


class TextSerializer(ModelSerializer):

    username = StringRelatedField(source="user", read_only=True)
    user = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())
    link = serializers.SerializerMethodField('get_link')

    class Meta:
        model = Text
        fields = ['id', 'value', 'created_at', 'user', "link", "username"]

    def get_link(self, obj):
        return "%stext/%s"%(settings.BASE_URL, obj.hash)

    def create(self, validated_data):
        validated_data['hash'] = secrets.token_hex(nbytes=16) # "%s/text/%s"%(settings.BASE_URL, )

        return super().create(validated_data)