from django.shortcuts import render

from watchlist_app.models import Movie
from django.http import JsonResponse


# //function based View class

'''WE HAVE TO FOLLOW THREE STEP TO RETURN OUR QUERY 1) WE HAVE TO EXTRACT ALL OF OUR OBJECTS ,
2) THEN WE HAVE TO CONVERT THEM IN PYTHON DICTIONARY
3) THEN BY USING JSONRESPONSE WE WILL CONVERT THE QUERY IN JSON FORMATE'''

def movie_list(request):
    
    '''WE will extract all the object here firslt then we will do our other task'''

# we have to return in json formate

    movies = Movie.objects.all()

    # //we can't print directly bcs right we not return anything

    # print(movies)# Not allowed
    '''For PRINTING THE VALUE HE HAVE TO USE:  #print(movies.values())'''
    

      #  WE will convert in list :

    data = {

        'movies':list(movies.values())
    
        }
  # Then we will return our json Response object
    return JsonResponse(data)

  
#   HOW WE WILL CHECL THAT OUR RESPONSE IS IN JSON THEN WE CAN VERIFY IT BY CHECKING THAT IN JSON 
#   1)BOLLEAN VALUE IS LIKE "true" and "false"
#   2) we can't use single quate in json


# For ectracting movie details we need to create our new view;


def movie_detail(request,pk): #pk is our primary key;

    movie = Movie.objects.get(pk=pk) # here we will check our primary key for specific object
    

    # WE will CONVERT RESPONSE IN DECTIONRY MANNUALLY
    data = {
        'name':movie.name, 
        'description':movie.description, 
        'active':movie.active, 
    }

    return JsonResponse(data)
   

 



   