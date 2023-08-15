from django.contrib import admin
from pages import views as pageviews
from users import views as userviews
from django.contrib.auth import views as authviews
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", pageviews.home, name="home"),
    path("register", userviews.user_register, name="register"),
    path("login", userviews.user_login, name="login"),
    path("logout", userviews.user_register, name="logout"),
    path("p", pageviews.page_profile,name="profile")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
