from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from .models import *


class Projects(viewsets.ModelViewSet):
    def get_queryset(self):
        get = self.request.query_params.get('get')
        size = self.request.query_params.get('size')
        if size is not None:
            self.pagination_class = PageNumberPagination
            PageNumberPagination.page_size = size
        if get is not None:
            queryset = Project.objects.prefetch_related('screenshots', 'timesheets').all()
        else:
            queryset = Project.objects.all()
        return queryset

    def get_serializer_class(self, *args, **kwargs):
        get = self.request.query_params.get('get')
        if get is not None:
            return SimpleProjectSerializer
        return ProjectSerializer


class ScreenShots(viewsets.ModelViewSet):
    serializer_class = ScreenShotSerializer
    queryset = ScreenShot.objects.all()

    def get_serializer_context(self):
        return {"project_id": self.kwargs["project_pk"]}

    def get_queryset(self):
        return ScreenShot.objects.filter(project=self.kwargs["project_pk"])


class TimeSheets(viewsets.ModelViewSet):
    serializer_class = TimeSheetSerializer
    queryset = TimeSheet.objects.all()

    def get_serializer_context(self):
        return {"project_id": self.kwargs["project_pk"]}

    def get_queryset(self):
        return TimeSheet.objects.filter(project=self.kwargs["project_pk"])
