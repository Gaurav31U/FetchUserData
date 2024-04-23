from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "CaptureUserData Admin"
admin.site.site_title = "CaptureUserData Admin Portal"
admin.site.index_title = "Welcome to CaptureUserData Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('UserData.urls')),
]
