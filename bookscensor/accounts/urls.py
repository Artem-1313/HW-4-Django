from django.urls import path, include
from .views import registration, RegistrationClass, LoginClass, LogoutClass

app_name="accounts"

urlpatterns = [
    path('registrsation/', RegistrationClass.as_view(), name="registration"),
    path('login/', LoginClass.as_view(), name="login"),
    path('logout/', LogoutClass.as_view(), name="logout"),


]