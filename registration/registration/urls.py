from django.contrib import admin
from django.urls import path, include
from form import views
# from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('admin/', admin.site.urls),
    path('', include('form.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)