from django.urls import path
from user.api.views import registration,logout
from rest_framework.authtoken.views import obtain_auth_token

app_name = "account"

urlpatterns = [
    path("login/" , obtain_auth_token , name="login"),
    path("registration/" , registration , name="registration"),
    path("logout/" , logout , name="logout"),
]
