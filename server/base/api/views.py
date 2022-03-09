from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from base.models import Note

from .serializers import NoteSerializer

#! ------ to customize the token claims "the embedded info of the token" ------ #
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
#* ---------------------------------------------------------------------------- #

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes= user.note_set.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

#! ----------------- to render all routes that our API serves ----------------- #
@api_view(['GET'])
def getRoutes(request):
   routes = [
      '/api/token',
      '/api/token/refresh',
   ]
   return Response(routes)
#* ---------------------------------------------------------------------------- #


