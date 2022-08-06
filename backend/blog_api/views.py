from rest_framework import generics
from blog.models import Post, Projects, Feedback, Nutrition
from .serializers import PostSerializer, FeedbackSerializer, ProjectsSerializer, NutritionSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission, IsAdminUser, DjangoModelPermissions, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend


class PostUserWritePermission(BasePermission):
    message = 'Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class PostDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = PostSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


class ProjectList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class NutritionList(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Nutrition.objects.all()
    serializer_class = NutritionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']


class ProjectDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProjectsSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Projects, slug=item)


class NutritionDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = NutritionSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Nutrition, slug=item)



class CreateFeedback(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = FeedbackSerializer
    parser_classes = [
        MultiPartParser,
        FormParser,
        JSONParser,
    ]

    def post(self, request, format=None):

        serializer = FeedbackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
