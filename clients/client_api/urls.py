# client_api/urls.py

from django.urls import include, path
from rest_framework import routers
from . import views
from files.views import UploadFileView

router = routers.DefaultRouter()
router.register(r'file', views.FileViewSet)
router.register(r'provider', views.ProviderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('upload/', UploadFileView.as_view(), name='upload-file')
]