from django.urls import path, include, re_path as url
from django.shortcuts import redirect
from django.views.generic import TemplateView

from rest_framework_nested import routers

from . import views

router = routers.DefaultRouter()
router.register("users", views.UserViewSet, basename="users")


class GoToApiPage(TemplateView):
    def get(self, request, **kwargs):
        return redirect("/auth/")

urlpatterns = [
    path("", include(router.urls)),
    # path("", include("djoser.urls")),
    path("jwt/create/", views.TokenView.as_view()),
    url(r"^(?P<path>.*)/$", GoToApiPage.as_view()),
]
