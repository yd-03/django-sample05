from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("todo.urls")),
    path("accounts/", include("allauth.urls")),
    path("upload_app/", include("upload_app.urls")),
]
