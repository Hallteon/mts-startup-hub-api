from django.contrib import admin
from django.urls import path, re_path, include

from startups.views import StartupsAPIList, StartupsAPIDetail, ProgramStartupsAPIList, StageStartupsAPIList, \
    ProgramsAPIList, StagesAPIList, StagesAPIDetail, ProgramsAPIDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/startups/', StartupsAPIList.as_view()),
    path('api/startups/program/<int:pk>/', ProgramStartupsAPIList.as_view()),
    path('api/startups/stage/<int:pk>/', StageStartupsAPIList.as_view()),
    path('api/startups/<int:pk>/', StartupsAPIDetail.as_view()),
    path('api/programs/', ProgramsAPIList.as_view()),
    path('api/stages/', StagesAPIList.as_view()),
    path('api/programs/<int:pk>/', ProgramsAPIDetail.as_view()),
    path('api/stages/<int:pk>/', StagesAPIDetail.as_view()),
    path('api/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
