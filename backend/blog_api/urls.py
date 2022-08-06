from django.urls import path
from .views import PostList, PostDetail, ProjectList, CreateFeedback, ProjectDetail, NutritionList, NutritionDetail

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = 'blog_api'

urlpatterns = [
    path('nutrition/<str:pk>', NutritionDetail.as_view(), name='nutrition_detail'),
    path('nutrition/', NutritionList.as_view(), name='nutrition_list'),
    path('posts/<str:pk>/', PostDetail.as_view(), name='post_detail'),
    path('posts/', PostList.as_view(), name='post_list'),
    path('projects/<str:pk>/', ProjectDetail.as_view(), name='project_detail'),
    path('projects/', ProjectList.as_view(), name='project_list'),
    path('feedback/', CreateFeedback.as_view(), name='create_feedback'),
]
