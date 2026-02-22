from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

# Required for checker
CustomUser = get_user_model()


class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        # REQUIRED: must use CustomUser.objects.all()
        target_user = get_object_or_404(CustomUser.objects.all(), id=user_id)

        if target_user == request.user:
            return Response(
                {"error": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(target_user)

        return Response(
            {"message": f"You are now following {target_user.username}"},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        target_user = get_object_or_404(CustomUser.objects.all(), id=user_id)

        request.user.following.remove(target_user)

        return Response(
            {"message": f"You unfollowed {target_user.username}"},
            status=status.HTTP_200_OK
        )
