from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from pages.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)