from django.contrib import admin
from pages import views
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
