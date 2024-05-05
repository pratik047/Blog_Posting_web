from django.urls import path
from .views_api import LoginView, RegisterView

# from .views import

urlpatterns = [path("login/", LoginView), path("register", RegisterView)]
