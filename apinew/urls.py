

from django.urls import path,include

# from apinew.views import movie_list,movie_detail

from apinew.views import MovieListAV,MovieDetailAV


urlpatterns = [

    path('list/', MovieListAV.as_view(),name='movie-list'),
    path('<int:pk>', MovieDetailAV.as_view(),name='movie-detail')
    
]