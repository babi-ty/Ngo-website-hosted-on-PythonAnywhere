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
    path('media/', views.media_page, name='media_page'),
    
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

    #Project Management
    path('dashboard/projects/', views.manage_project, name='dashboard_manage_project'),
    path('dashboard/projects/add/', views.manage_project_add, name='dashboard_manage_project_add'),
    path('dashboard/projects/edit/<int:pk>/', views.manage_project_edit, name='dashboard_manage_project_edit'),
    path('dashboard/projects/delete/<int:pk>/', views.manage_project_delete, name='dashboard_manage_project_delete'),

        #media Pages
    path('dashboard/media/', views.manage_media_home, name='dashboard_manage_media_home'),
     # Press Release Management
    path('dashboard/press-releases/', views.manage_press_release, name='dashboard_manage_press_release'),
    path('dashboard/press-releases/add/', views.manage_press_release_add, name='dashboard_manage_press_release_add'),
    path('dashboard/press-releases/edit/<int:pk>/', views.manage_press_release_edit, name='dashboard_manage_press_release_edit'),
    path('dashboard/press-releases/delete/<int:pk>/', views.manage_press_release_delete, name='dashboard_manage_press_release_delete'),
    
    # Media Coverage Management
    path('dashboard/media-coverage/', views.manage_media_coverage, name='dashboard_manage_media_coverage'),
    path('dashboard/media-coverage/add/', views.manage_media_coverage_add, name='dashboard_manage_media_coverage_add'),
    path('dashboard/media-coverage/edit/<int:pk>/', views.manage_media_coverage_edit, name='dashboard_manage_media_coverage_edit'),
    path('dashboard/media-coverage/delete/<int:pk>/', views.manage_media_coverage_delete, name='dashboard_manage_media_coverage_delete'),
    
    # Gallery Management
    path('dashboard/gallery/', views.manage_gallery, name='dashboard_manage_gallery'),
    path('dashboard/gallery/add/', views.manage_gallery_add, name='dashboard_manage_gallery_add'),
    path('dashboard/gallery/edit/<int:pk>/', views.manage_gallery_edit, name='dashboard_manage_gallery_edit'),
    path('dashboard/gallery/delete/<int:pk>/', views.manage_gallery_delete, name='dashboard_manage_gallery_delete'),
    
    # Video Management
    path('dashboard/videos/', views.manage_video, name='dashboard_manage_video'),
    path('dashboard/videos/add/', views.manage_video_add, name='dashboard_manage_video_add'),
    path('dashboard/videos/edit/<int:pk>/', views.manage_video_edit, name='dashboard_manage_video_edit'),
    path('dashboard/videos/delete/<int:pk>/', views.manage_video_delete, name='dashboard_manage_video_delete'),
    
    # Media Contact Management
    path('dashboard/media-contacts/', views.manage_media_contact, name='dashboard_manage_media_contact'),
    path('dashboard/media-contacts/add/', views.manage_media_contact_add, name='dashboard_manage_media_contact_add'),
    path('dashboard/media-contacts/edit/<int:pk>/', views.manage_media_contact_edit, name='dashboard_manage_media_contact_edit'),
    path('dashboard/media-contacts/delete/<int:pk>/', views.manage_media_contact_delete, name='dashboard_manage_media_contact_delete'),

]