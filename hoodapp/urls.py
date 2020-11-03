from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^my-profile/',views.my_profile, name='my-profile'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
    url(r'^notifications',views.notification, name='notifications'),
    url(r'^new/notification$',views.new_notification, name='new-notification'),
    url(r'^new/business$',views.new_business, name='new-business'),
    url(r'^businesses',views.businesses, name='businesses'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)