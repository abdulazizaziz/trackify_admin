from django.urls import path, include
from projects import views as project_view

from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register('projects', project_view.Projects, basename='projects')

project_router = routers.NestedDefaultRouter(router, 'projects', lookup='project')
project_router.register('screenshots', project_view.ScreenShots, basename='project-screenshtos')
project_router.register('timesheets', project_view.TimeSheets, basename='timesheet-screenshtos')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
]
