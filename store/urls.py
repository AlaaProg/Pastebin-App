from django.urls import path
from rest_framework import routers
from store.views import UserTextViewSet, read_text


router = routers.DefaultRouter()

router.register(r'', UserTextViewSet)
urlpatterns = [
    path("link/<hash>", read_text, name="read_text_by_hash")
]
urlpatterns += router.urls