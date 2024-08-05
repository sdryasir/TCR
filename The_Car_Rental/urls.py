"""
URL configuration for The_Car_Rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static






urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage),
    path('about/', views.aboutPage, name='about'),
    path('login/', views.loginPage, name='login'),
    path('create-new-account/', views.Create_accountPage, name='create_account'),
    path('our-cars/', views.Our_carsPage, name='our_cars'),
    path('car-detail/<id>', views.Car_detailPage, name='car_detail'),
    path('faq/', views.faqPage, name='faq'),
    path('contact/', views.contactPage, name='contact'),
    path('save-contact/', views.saveContact, name='save-contact'),
    path('our-team/', views.Our_teamPage, name='our_team'),
    path('blog/', views.blogPage, name='blog'),
    path('single-post/<id>', views.Single_postPage, name='single_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  





