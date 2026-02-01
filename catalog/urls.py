from django.urls import path
from . import views



#ΔΗΜΙΟΥΡΓΩ ΤΟ path GIA mobile_list + mobile_detail + About us
urlpatterns = [

    path('', views.mobile_list, name='mobile_list'),
    path('mobile/<int:pk>/', views.mobile_detail, name='mobile_detail'),
    path('about/', views.about_us, name='about_us'),

]
