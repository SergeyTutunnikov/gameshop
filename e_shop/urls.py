from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from pages.views import home_page,ShopPage,GamePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page),
    path('shop/',ShopPage.as_view(),name='shop'),
    path('shop/<slug:slug>',GamePage.as_view(),name='detail')
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)