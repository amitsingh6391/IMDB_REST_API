

from django.urls import path,include

# from apinew.views import movie_list,movie_detail

from apinew.views import WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV


urlpatterns = [

    path('list/', WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>', WatchDetailAV.as_view(),name='movie-detail'),
    path('stream/',StreamPlatformAV.as_view(),name='stream-platform'),
    path('stream/<int:pk>', StreamPlatformDetailAV.as_view(),name='streamPlatform-detail'),
    
]
