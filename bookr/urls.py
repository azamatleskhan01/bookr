from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import include, path
from reviews.views import profile
from django.contrib import admin
urlpatterns = [
    # Административная панель
    path("filter_demo/", include("filter_demo.urls")),
    path("admin/", admin.site.urls),

    # Аутентификация
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),

    path('accounts/profile/',profile, name ='profile'),
    # Основные страницы
    path("", include("reviews.urls")),
    path("book_management/", include("book_management.urls")),
]

# Подключение медиафайлов в режиме отладки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
