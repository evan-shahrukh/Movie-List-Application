from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
# from rest_framework import mixins
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404
from django.db.models import Sum

from watchlist_app.models import WatchList,StreamingPlatform,Review
from watchlist_app.api.serializers import WatchListSerializer,StreamingPlatformSerializer,ReviewSerializer
from watchlist_app.api.permissions import AdminOrReadOnly,ReviewUserOrReadOnly

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == "GET":
#         movie = Movie.objects.all()
#         serializer = MovieSerializer(movie , many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     if request.method == "POST":
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET","PUT","DELETE"])
# def movie_details(request,id):
#     if request.method == "GET":
#         try:
#             movie = Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
#     if request.method == "PUT":
#         try:
#             movie = Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = MovieSerializer(movie,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == "DELETE":
#         try:
#             movie = Movie.objects.get(id=id)
#         except Movie.DoesNotExist:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class StreamingPlatformAV(APIView):
#     def get(self,request):
#         platform = StreamingPlatform.objects.all()
#         serializer = StreamingPlatformSerializer(platform,many=True,context={'request': request})
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self,request):
#         serializer = StreamingPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
# class StreamingPlatformDetailAV(APIView):
#     def get(self,request,pk):
#         try:
#             platform = StreamingPlatform.objects.get(pk=pk)
#         except StreamingPlatform.DoesNotExist:
#             return Response("No Data Found.",status=status.HTTP_404_NOT_FOUND)
#         serializer = StreamingPlatformSerializer(platform,context={"request" : request})
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def put(self,request,pk):
#         try:
#             platform = StreamingPlatform.objects.get(pk=pk)
#         except StreamingPlatform.DoesNotExist:
#             return Response("No Data Found.",status=status.HTTP_404_NOT_FOUND)
#         serializer = StreamingPlatformSerializer(platform,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         try:
#             platform = StreamingPlatform.objects.get(pk=pk)
#         except StreamingPlatform.DoesNotExist:
#             return Response("No Data Found.",status=status.HTTP_404_NOT_FOUND)
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class StreamingPlatformVS(viewsets.ViewSet):
    
#     def list(self,request):
#         queryset = StreamingPlatform.objects.all()
#         serializer = StreamingPlatformSerializer(queryset,many=True,context={'request' : request})
#         return Response(serializer.data)
    
#     def retrieve(self,request,pk=None):
#         queryset = StreamingPlatform.objects.all()
#         platform = get_object_or_404(queryset,pk=pk)
#         serializer = StreamingPlatformSerializer(platform,context={'request' : request})
#         return Response(serializer.data)
    
#     def create(self,request):
#         serializer = StreamingPlatformSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
    
#     def update(self,request,pk=None):
#         queryset = StreamingPlatform.objects.all()
#         platform = get_object_or_404(queryset,pk=pk)
#         serializer = StreamingPlatformSerializer(platform,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#     def delete(self,request,pk=None):
#         queryset = StreamingPlatform.objects.all()
#         platform = get_object_or_404(queryset,pk=pk)
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class StreamingPlatformVS(viewsets.ModelViewSet):
    permission_classes = [AdminOrReadOnly]
    queryset = StreamingPlatform.objects.all()
    serializer_class = StreamingPlatformSerializer

class WatchListAV(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        movie = WatchList.objects.all()
        serializer = WatchListSerializer(movie,many=True,context={"request" : request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WatchDetailAV(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response("No Data Found.",status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie,context={"request" : request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response("No Data Found.",status=status.HTTP_404_NOT_FOUND)
        serializer = WatchListSerializer(movie,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response("No Data Found.",status=status.HTTP_404_NOT_FOUND)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
#     def delete(self,request,*args,**kwargs):
#         return self.delete(request,*args,**kwargs)

class ReviewList(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.filter(watchlist=self.kwargs["pk"])
           

class ReviewCreate(generics.CreateAPIView):
    permission_classes = [ReviewUserOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def perform_create(self,serializer):
        watchlist = WatchList.objects.get(pk=self.kwargs.get("pk"))
        review_user = Review.objects.filter(review_user=self.request.user)
        
        if review_user.exists():
            raise ValidationError('User has already reviewed this movie.')
        
        if watchlist.number_of_rating == 0:
            watchlist.number_of_rating = watchlist.number_of_rating + 1
            watchlist.avg_rating = serializer.validated_data["rating"]
        else:
            watchlist.number_of_rating = watchlist.number_of_rating + 1
            watchlist.avg_rating = ( Review.objects.filter(watchlist=self.kwargs.get("pk")).aggregate(Sum("rating"))["rating__sum"] + int(serializer.validated_data["rating"]) )/ watchlist.number_of_rating
        
        watchlist.save()
        serializer.save(watchlist=watchlist,review_user=self.request.user)
    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ReviewUserOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
class ReviewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    
class ReviewDestroy(generics.RetrieveDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer