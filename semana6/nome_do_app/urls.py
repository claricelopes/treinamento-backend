from django.contrib import admin 
from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AppViewSet


router = DefaultRouter()

router.register('', AppViewSet) 

urlpatterns = router.urls 