from rest_framework_simplejwt.views import TokenObtainPairView as BaseTokenView

from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from djoser.views import UserViewSet as BaseUserViewSet
from rest_framework.pagination import PageNumberPagination

from .serializers import *
from .models import *



class TokenView(BaseTokenView):
    serializer_class = TokenSerializer



class UserViewSet(BaseUserViewSet):
    search_fields = ["name", "email"]

    def get_queryset(self):
        queryset = User.objects.all()
        size = self.request.query_params.get("size")
        if size is not None:
            self.pagination_class = PageNumberPagination
            PageNumberPagination.page_size = size
        return queryset


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.is_superuser:
            return Response(status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
