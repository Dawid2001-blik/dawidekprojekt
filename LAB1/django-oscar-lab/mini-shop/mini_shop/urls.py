from django.contrib import admin
from django.urls import include, path
from django.apps import apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(apps.get_app_config('oscar').urls[0])),
]