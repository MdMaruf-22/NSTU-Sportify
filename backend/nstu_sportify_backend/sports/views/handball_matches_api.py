from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ..models import Matchdetails
from ..serializers import MatchdetailsWithTeamsSerializer
from ..permission import IsAdminOrReadOnly

class HandballMatchesAPIView(APIView):
    def get_permissions(self):
        if self.request.method in ['POST', 'PUT', 'PATCH', 'DELETE']:
            return [IsAdminOrReadOnly()]
        return [AllowAny()]

    def get(self, request):
        handball_matches = Matchdetails.objects.filter(sport='handball')
        serializer = MatchdetailsWithTeamsSerializer(handball_matches, many=True)
        return Response(serializer.data)
