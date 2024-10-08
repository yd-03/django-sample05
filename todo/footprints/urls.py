from . import views
from django.urls import path

urlpatterns = [
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("user/", views.user_view, name="user"),
    path("others/", views.others_view, name="others"),
    path("other/<int:id>/", views.other_view, name="other"),
]
