from django.contrib import admin
from django.urls import path, include
from task.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/tasks/', include('task.urls')),
    path('api/users/', include('users.urls')),
    path("api/ai/", include("ai.urls")),
]
