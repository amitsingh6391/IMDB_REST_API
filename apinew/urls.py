

from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from apinew.views import movie_list,movie_detail

from apinew.views import (StreamPlatformVs, WatchListAV,WatchDetailAV,
StreamPlatformAV,StreamPlatformDetailAV,ReviewList,ReviewDetail,ReviewCreate
)


router = DefaultRouter()
router.register('stream',StreamPlatformVs,basename="streamplatform")

urlpatterns = [

    path('list/', WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(),name='movie-detail'),

    path('',include(router.urls)),

    # path('stream/',StreamPlatformAV.as_view(),name='stream-platform'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(),name='streamPlatform-detail'),
  
    # path('review',ReviewList.as_view(),name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(),name='review-list'),


    path('<int:pk>/reviews', ReviewList.as_view(),name='review-list'),
    path('<int:pk>/review-create', ReviewCreate.as_view(),name='review-create'),
    path('review/<int:pk>', ReviewDetail.as_view(),name='review-detail')

]
