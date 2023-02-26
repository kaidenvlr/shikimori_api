from django.contrib import admin
from django.urls import path, include

from animestorage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/anime/', views.AnimeAPIList.as_view()),
    path('api/v1/anime/<int:pk>/', views.AnimeAPIRetrieveUpdateDestroy.as_view()),
]
