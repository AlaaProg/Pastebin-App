
from django.urls import re_path
from app.views import index

urlpatterns = [
    re_path("^.*$", index, name="home")
]

    