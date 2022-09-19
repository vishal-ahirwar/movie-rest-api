from rest_framework.response import Response
from .serializers import MovieSerializer
from rest_framework.views import APIView
from database.models import Movie
class MovieAPIView(APIView):
    def get(self,request):
        movies=Movie.objects.all()
        m=MovieSerializer(movies,many=True)
        return Response({"movies":m.data})
        
    def post(self,request):
        new_movie=MovieSerializer(data=request.data)
        if new_movie.is_valid():
            new_movie.save()
            return Response({"Movie Added":new_movie.data})
        else:
            return Response({"error":"bad data!"})

