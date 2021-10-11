from rest_framework.response import Response
from .models import WatchList,StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer
from rest_framework.views import APIView
from rest_framework import status


# // ********** CLASS BASED VIEW *******//

class StreamPlatformAV(APIView):

    def get(self,request):

        streamPlatform = StreamPlatform.objects.all()
        serializer =  StreamPlatformSerializer(streamPlatform,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
           
            return Response(serializer.data)
        else:
           
            return Response(serializer.errors)


 # DEfine class for stream polatform details View:

class StreamPlatformDetailAV(APIView):

    # Find a particular stream Platform 

    def get(self,request,pk):
        try:
            streamPlatform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({"Error":"StreamPlatform not found"},status=status.HTTP_404_NOT_FOUND)
       
        serializer = StreamPlatformSerializer(streamPlatform)
        return Response(serializer.data)

# For Update details of particular Stram Fields;
    
    def put(self, request,pk):
        streamPlatform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(streamPlatform,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
# For delete a particular Stream platform from our database we will use this method;

    def delete(self,request,pk):
        streamPlatform = StreamPlatform.objects.get(pk=pk)
        streamPlatform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class WatchListAV(APIView):

    def get(self, request):

        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies,many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # print("this is valid case in post request")
            return Response(serializer.data)
        else:
            # print("this is error case in post request")
            return Response(serializer.errors)


class WatchDetailAV(APIView):

    def get(self, request,pk):
        try:
            movie= WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'error': 'Movie not found'},status=status.HTTP_404_NOT_FOUND)

        serializer = WatchListSerializer(movie)
        return Response(serializer.data)
    def put(self, request,pk):
        movie= WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self, request,pk):
        movie= WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)










# //*************** FUNCTION BASED VIEW ************//


# @api_view(['GET','POST'])
# def movie_list(request):
#     if(request.method == 'GET'):
#         movies = Movie.objects.all()
#         serializer= MovieSerializer(movies,many=True)
#         return Response(serializer.data)
#     if(request.method == 'POST'):
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
          


# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,pk):
#     if(request.method == 'GET'):

#         try:
#             movie= Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'error': 'Movie not found'},status=status.HTTP_404_NOT_FOUND)

#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#      #   in put we are updating datawhole but in patch we are updating data partialy;
#     if(request.method == 'PUT'): 
#         movie= Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():

#             serializer.save()
#             return Response(serializer.data)
#         else:

#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    
    # if(request.method == 'DELETE'):
    #     movie= Movie.objects.get(pk=pk)
    #     movie.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)



