from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_200_OK,
)
from rest_framework.response import Response
from rest_framework import generics, permissions

from .serializers import UserSerializer, UserSigninSerializer
from .models import User
from .permissions import IsSelf


@api_view(["POST"])
@permission_classes((permissions.AllowAny,))
def login(request):
    # Auth
    signin_serializer = UserSigninSerializer(data=request.data)
    if not signin_serializer.is_valid():
        return Response(signin_serializer.errors, status=HTTP_400_BAD_REQUEST)

    user = authenticate(
        username=signin_serializer.data["username"],
        password=signin_serializer.data["password"],
    )
    if not user:
        return Response(
            {"detail": "Invalid Credentials or activate account"},
            status=HTTP_401_UNAUTHORIZED,
        )

    user_serialized = UserSerializer(user, context={"request": request})

    return Response({"user": user_serialized.data,}, status=HTTP_200_OK,)


class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, IsSelf]
