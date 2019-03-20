from django.contrib import admin
from django.urls import path
from wineapp.views import search, home, aboutus, contactus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('search/', search, name="search"),
    path('aboutus/', aboutus, name = "aboutus"),
    path('contactus/', contactus, name = "contactus"),
    path('', home, name = "home"),
    path('home', home, name = "home"),
]
