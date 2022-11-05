from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('bustracker/', include('bustracker.urls')),
    path('', include('bustracker.urls')),
    path('admin/', admin.site.urls),
]
