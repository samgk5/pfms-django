from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sam_apcs.urls')),  # ✅ include your app's URLs here
]

