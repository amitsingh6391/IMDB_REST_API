from rest_framework.response import Response
from .models import Review, WatchList,StreamPlatform
from .serializers import WatchListSerializer, StreamPlatformSerializer,ReviewSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics
# from rest_framework import mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404



class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        serializer.save(watchlist=movie)

# // ListCreateAPIView will give us post method also but in ListView we don't have'

class ReviewList(generics.ListAPIView):

    #  queryset = Review.objects.all()

     serializer_class = ReviewSerializer

     def get_queryset(self):
         pk = self.kwargs['pk']
         return Review.objects.filter(watchlist=pk)

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Review.objects.all()
     serializer_class = ReviewSerializer

#  class ReviewDetails(mixins.RetrieveModelMixin, 
#                     generics.GenericAPIView):

#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer


#     def get(self, request, *args, **kwargs):

#         return self.retrieve(request, *args, **kwargs)




# class ReviewList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)




# ViewSets 'While" using Router ;


class StreamPlatformVs(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    


       #  ''''' ViewSets .ViewSets ************8///

# class StreamPlatformVs(viewsets.ViewSet):
#    def list(self, request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#    def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)
    
#    def create(self, request):
#         serializer = StreamPlatformSerializer(data = request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
           
#             return Response(serializer.data)
#         else:
           
#             return Response(serializer.errors)
    
#    def destroy(self, request,pk):
#         streamPlatform = StreamPlatform.objects.get(pk=pk)
#         streamPlatform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)







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



