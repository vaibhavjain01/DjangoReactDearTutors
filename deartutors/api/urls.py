from rest_framework import routers
from django.contrib import admin
from django.urls import path
from .api import TestViewSet, AddressView, ContactNumberView, CategoryView, \
    AboutUsView, HoursOfOperationView, ServiceView, CategoryServiceView, \
    ServiceImageView, ServiceImageListView, BrandLogoView, BrandWebPageLogoView, \
    ServiceThumbView, AboutUsImageView, AboutUsResumeView, FileUploadView, \
    ContactUsView, BrandView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', TestViewSet.as_view({'get': 'list'})),
    path('brand/', BrandView.as_view({'get': 'list'})),
    path('address/', AddressView.as_view({'get': 'list'})),
    path('contact/', ContactNumberView.as_view({'get': 'list'})),
    path('categories/', CategoryView.as_view({'get': 'list'})),
    path('aboutus/', AboutUsView.as_view({'get': 'list'})),
    path('hoursofoperation/', HoursOfOperationView.as_view({'get': 'list'})),
    path('services/', ServiceView.as_view({'get': 'list'})),
    path('services/<str:category>', CategoryServiceView.as_view()),
    path('serviceimages/', ServiceImageView.as_view({'get': 'list'})),
    path('servicelist/', ServiceImageListView.as_view()),
    path('media/images/brand_logo/<str:img_name>', BrandLogoView.as_view()),
    path('media/images/brand_web_page_logo/<str:img_name>', BrandWebPageLogoView.as_view()),
    path('media/images/service/thumb/<str:img_name>', ServiceThumbView.as_view()),
    path('media/images/aboutus/<str:img_name>', AboutUsImageView.as_view()),
    path('media/uploaded/resume/<str:file_name>', AboutUsResumeView.as_view()),
    path(r'upload/', FileUploadView.as_view()),
    path('contactus/', ContactUsView.as_view()),
]