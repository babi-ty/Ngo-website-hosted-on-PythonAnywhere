from django.urls import path
from . import views

urlpatterns = [
    # Public Pages
    path('', views.Home, name='home'),
    path('rescue/', views.rescue_page, name='rescue'),
    path('surgery/', views.surgery_page, name='surgery'),
    path('adopt/', views.adopt_page, name='adopt'),
    path('volunteer/', views.volunteer_page, name='volunteer'),
    path('donate/', views.donate_page, name='donate'),
    path('whoarewe/', views.who_are_we_page, name='whoarewe'),
    path('whatwedo/', views.what_we_do_page, name='whatwedo'),
    path('waystohelp/', views.ways_to_help_page, name='waystohelp'),
    
    # Dashboard Home
    path('dashboard/', views.dashboard_home, name='dashboard_home'),
    
    # Banner (Slider) Management
    path('dashboard/manage-slider/', views.manage_image_slider, name='dashboard_manage_slider'),
    path('dashboard/manage-slider/add/', views.manage_slider_add, name='dashboard_manage_slider_add'),
    path('dashboard/manage-slider/edit/<int:pk>/', views.manage_slider_edit, name='dashboard_manage_slider_edit'),
    path('dashboard/manage-slider/delete/<int:pk>/', views.manage_slider_delete, name='dashboard_manage_slider_delete'),

    # Statistic Management
    path('dashboard/manage-statistic/', views.manage_statistic, name='dashboard_manage_statistic'),
    path('dashboard/manage-statistic/add/', views.manage_statistic_add, name='dashboard_manage_statistic_add'),
    path('dashboard/manage-statistic/edit/<int:pk>/', views.manage_statistic_edit, name='dashboard_manage_statistic_edit'),
    path('dashboard/manage-statistic/delete/<int:pk>/', views.manage_statistic_delete, name='dashboard_manage_statistic_delete'),
    
    # Vision & Mission Management
    path('dashboard/manage-vision/', views.manage_vision, name='dashboard_manage_vision'),
    
    # Initiative Management
    path('dashboard/manage-initiative/', views.manage_initiative, name='dashboard_manage_initiative'),
    path('dashboard/manage-initiative/add/', views.manage_initiative_add, name='dashboard_manage_initiative_add'),
    path('dashboard/manage-initiative/edit/<int:pk>/', views.manage_initiative_edit, name='dashboard_manage_initiative_edit'),
    path('dashboard/manage-initiative/delete/<int:pk>/', views.manage_initiative_delete, name='dashboard_manage_initiative_delete'),
]