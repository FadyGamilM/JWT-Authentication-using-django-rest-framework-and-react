from rest_framework.response import Response
from rest_framework.decorators import api_view

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

#! ----------------- to render all routes that our API serves ----------------- #
def getRoutes(request):
   routes = [
      '/api/token',
      '/api/token/refresh',
   ]
   return Response(routes)
#* ---------------------------------------------------------------------------- #
