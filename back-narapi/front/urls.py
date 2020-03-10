
from django.contrib import admin
from django.urls import path
from django.urls import include, path
from rest_framework import routers
from core.views import CharacterViewSet

router = routers.DefaultRouter()
router.register(r'characters', CharacterViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
