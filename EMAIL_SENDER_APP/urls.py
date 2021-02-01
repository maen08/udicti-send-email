
from django.contrib import admin
from django.urls import path, include
from main_app import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('rest_framework.urls')),
    path('', views.sender_view),
    path('get/', views.test_view),
    path('register/', views.register),
    # path('login/', views.signin),
    path('auth/', obtain_auth_token),     # get the token page
    path('create/', views.create_email_view, name='create'),
]
