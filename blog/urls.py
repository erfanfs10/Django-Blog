from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('bl/admin/', admin.site.urls),
    path('bl/', include('core.urls')),
    path('bl/auth/', include('authentication.urls')),
    path('bl/i18n/', include('django.conf.urls.i18n'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
