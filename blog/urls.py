from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='resume.html')),
    path('blog/admin/', admin.site.urls),
    path('blog/', include('core.urls')),
    path('blog/auth/', include('authentication.urls')),
    path('blog/i18n/', include('django.conf.urls.i18n')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
