from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('ogalogo/', admin.site.urls),
    path('api/',include('todoapps.urls')),
]