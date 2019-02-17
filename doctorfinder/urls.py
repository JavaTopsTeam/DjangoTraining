from django.urls import path,include
from . import views
urlpatterns = [

    # Page Url
    path('register/',views.RegistrationPage,name="regsiter"),
    path('login/',views.LoginPage,name="login"),
    path('forgot/',views.ForgotPage,name="forgot"),


    # Page Functionality Url
    path('userregistration/',views.registeruser,name="userregistration"),
    path('userlogin/',views.loginuser,name="userlogin"),
    path('userforgotemailverify/',views.userforgot_email_verify,name="userforgotemailverify"),
    path('resetPassword/',views.resetPassword,name="resetPassword"),




]
