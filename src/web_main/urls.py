from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from stac_iitmandi import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("stac_iitmandi.urls")),
    path("update_server/", views.update_, name="update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
