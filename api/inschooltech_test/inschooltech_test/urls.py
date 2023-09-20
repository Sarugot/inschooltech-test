from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('indicators.urls')),
    path('api/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.authtoken')),
]