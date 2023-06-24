from django.contrib import admin
from django.urls import path, include
from Authentication import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Authentication.urls')),
    path('', views.index, name='home'),
]
