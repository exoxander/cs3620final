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
    path("logout", userviews.user_logout, name="logout"),
    path("p/<int:profile_id>", pageviews.page_profile,name="profile"),
    path("profileredirect", pageviews.profile_redirect,name="profileredirect"),
    path("postupsert", pageviews.post_upsert,name="postupsert"),
    path("search", pageviews.search,name="search"),
    path("post/<int:post_id>", pageviews.post_details,name="post"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
