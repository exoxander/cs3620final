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
    path("register", userviews.register, name="register"),
    path("login", userviews.user_login, name="login"),
    path("logout", authviews.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
