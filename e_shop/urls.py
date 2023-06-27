from django.contrib import admin
from django.contrib.auth.views import PasswordChangeView,PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from pages.views import home_page,ShopPage,GamePage
from accounts.views import LoginPage,sign_out,RegisterPage,activate_page
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_page,name='home'),
    path('shop/',ShopPage.as_view(),name='shop'),
    path('shop/<slug:slug>',GamePage.as_view(),name='detail'),
    path('login/',LoginPage.as_view(),name='login'),
    path('logout/',sign_out,name='log_out'),
    path('signup/',RegisterPage.as_view(),name='register'),
    path('activate/<uidb64>/<token>',activate_page,name='activate_account'),
    
    path('password_change/',PasswordChangeView.as_view(template_name='password_change_form.html'),name='password_change'),
    path('password_change_done/',PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),
    path('password_reset/',PasswordResetView.as_view(template_name='password_reset_form.html',email_template_name='password_reset_email.html'),name='password_reset'),
    path('password_reset_done/',PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password_reset/<uidb64>/<token>',PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete')
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)