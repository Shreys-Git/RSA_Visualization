from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mychat.urls')),
    path('keys/', include('mychat.urls')),
    path('encrypted/', include('mychat.urls')),
    
]
