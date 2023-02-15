from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('auth/', include('authentication.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('i18n/', include('django.conf.urls.i18n')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
