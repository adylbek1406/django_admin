from django.urls import path
from . views import ProductView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("api/",ProductView.as_view({"get":"list"})),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)