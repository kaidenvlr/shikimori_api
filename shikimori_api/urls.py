from django.contrib import admin
from django.urls import path, include

from animestorage import views

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),

    # auth
    path('api/v1/auth/', include('rest_framework.urls')),

    # animestorage

    # anime
    path('api/v1/anime/', views.AnimeAPIListCreate.as_view()),
    path('api/v1/anime/<int:pk>/', views.AnimeAPIRetrieveUpdateDestroy.as_view()),
    # anime type
    path('api/v1/animetype/', views.AnimeTypeAPIListCreate.as_view()),
    path('api/v1/animetype/<int:pk>/', views.AnimeTypeAPIRetrieveUpdateDestroy.as_view()),
    # status
    path('api/v1/status/', views.StatusAPIListCreate.as_view()),
    path('api/v1/status/<int:pk>/', views.StatusAPIRetrieveUpdateDestroy.as_view()),
    # genre
    path('api/v1/genre/', views.GenreAPIListCreate.as_view()),
    path('api/v1/genre/<int:pk>/', views.GenreAPIRetrieveUpdateDestroy.as_view()),
    # age rating
    path('api/v1/age-rating/', views.AgeRatingAPIListCreate.as_view()),
    path('api/v1/age-rating/<int:pk>/', views.AgeRatingAPIRetrieveUpdateDestroy.as_view()),
    # studio
    path('api/v1/studio/', views.StudioAPIListCreate.as_view()),
    path('api/v1/studio/<int:pk>/', views.StudioAPIRetrieveUpdateDestroy.as_view()),

    # userstorage

]
