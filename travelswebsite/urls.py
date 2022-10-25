
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('book',views.book,name='book'),
    path('package',views.package,name='package'),
    path('services',views.services,name='services'),
    path('handleLogin',views.handleLogin,name='Login'),
    path('handleLogout',views.handleLogout,name='Logout'),
    path('handleSignup',views.handleSignup,name='Signup'),
    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)