from django.urls import path
from .views import PersonAPI

urlpatterns = [
    path('persons', PersonAPI.as_view()),           # GET(전체), POST, PUT
    path('persons/<int:seq>', PersonAPI.as_view())  # GET(상세), DELETE
]