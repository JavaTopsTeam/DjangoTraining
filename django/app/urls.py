from django.urls import path,include
from . import views
urlpatterns = [

    path('registerpage/',views.RegistrationPage,name="register"),
    path('user_register/',views.user_register,name="user_register"),
    path('userformregister/',views.UserFormRegister,name="userformregister"),
    path('userinfo/',views.user_form_register,name='userinfo'),
]
