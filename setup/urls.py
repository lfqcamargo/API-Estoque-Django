from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from materiais.views import MateriaisViewSet

router = routers.DefaultRouter()
router.register('materiais', MateriaisViewSet, basename='Materiais')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
