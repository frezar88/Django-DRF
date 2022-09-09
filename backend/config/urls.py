from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static

from posts.views import PostViewSet

scheme_view = get_swagger_view(title="Demo Api")
router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger/', scheme_view),
    path('videos/', include('videos.urls')),

]

urlpatterns += router.urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
