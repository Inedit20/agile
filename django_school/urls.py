from django.urls import include, path
from django.contrib import admin

from classroom.views import classroom, students, teachers



urlpatterns = [
    path('', include('classroom.urls')),
     path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
   

]
