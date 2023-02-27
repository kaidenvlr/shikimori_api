from django.contrib import admin
from django.urls import path, include

from animestorage import views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # animestorage
    # auth
    path('api/v1/auth/', include('rest_framework.urls')),
    # anime
    path('api/v1/anime/', views.AnimeAPIList.as_view()),
    path('api/v1/anime/<int:pk>/', views.AnimeAPIRetrieveUpdateDestroy.as_view()),
    # anime type
    path('api/v1/animetype/', views.AnimeTypeAPIList.as_view()),
    path('api/v1/animetype/<int:pk>/', views.AnimeTypeAPIRetrieveUpdateDestroy.as_view()),

    # userstorage
]
