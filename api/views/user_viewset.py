from rest_framework.views import APIView
from ..serializers.user_serializer import UserSerializer
from rest_framework.response import Response
import rest_framework.status as status
from ..models import User
from rest_framework import permissions


class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Return a list of all users.
        """

        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)

        return Response(users_serializer.data, status=status.HTTP_200_OK)
