from django.urls import path, include
from rest_framework import routers
from backoffice_engine.views import Home

router = routers.SimpleRouter()

urlpatterns = [
    path('', Home, name='home'),
    path('', include(router.urls)),
]
