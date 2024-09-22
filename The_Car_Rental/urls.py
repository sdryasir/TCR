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
    path('', views.homePage, name='home'),
    path('add-your-car', views.addyourCarPage, name='addyourcar'),
    path('car-added', views.addyourCar, name='caradded'),
    path('Car-Submission-Acknowledged', views.car_added, name='caraddedsuccessfully'),
    path('submission-unsuccessful', views.car_failed, name='carfailed'),
    path('about/', views.aboutPage, name='about'),
    path('login/', views.loginPage, name='login'),
    path('create-new-account/', views.Create_accountPage, name='create_account'),
    path('Create_accountPage-user/', views.Create_accountPageUser, name='Create_accountPage-user'),
    path('login-user/', views.loginUser, name='login-user'),
    path('logout-user/', views.logoutUser, name='logout-user'),
    path('our-cars/', views.Our_carsPage, name='our_cars'),
    path('car-detail/<id>', views.Car_detailPage, name='car_detail'),
    path('faq/', views.faqPage, name='faq'),
    path('contact/', views.contactPage, name='contactPage'),
    path('save-contact/', views.saveContact, name='save-contact'),
    path('quick-book/', views.quick_Book, name='quick-book'),
    path('our-team/', views.Our_teamPage, name='our_team'),
    path('blog/', views.blogPage, name='blog'),
    path('single-post/<id>', views.Single_postPage, name='single_post'),
    path('checkout/', views.checkout_view, name='checkout'),

    path('create-checkout-session/', views.checkout_session, name='create-checkout-session'),

    path('process_checkout/', views.process_checkout, name='order_confirmation'),
    path('payment-success/', views.successPage, name='success'),
    path('payment-failed/', views.cancelPage, name='cancel'),
    path('booking-confirmed/', views.Booking_Corfirmed_Page, name='Booking-Confirmed'),
    path('booking-failed/', views.Booking_Failed_Page, name='Booking-Failed'),


    path('process_checkout/', views.process_checkout, name='process_checkout'),

    path('success/', views.successPage, name='success'),
    path('cancel/', views.cancelPage, name='cancel'),
    

    

    path('order_status/', views.orderStatus, name='order_status'),
    path('delete_order/<int:order_id>/', views.delete_order, name='delete_order'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('reservation/',views.cart_detail,name='reservation'),


    path('subscribe/', views.subscribe, name='subscribe'),







]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  





