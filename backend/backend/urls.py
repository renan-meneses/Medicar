"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Medica API",
        default_version="v1",
        description="Sistema voltado a gerenciamento de clinica medica",
        terms_of_service="https://www.google.com/policies/terms/",
        #   contact=openapi.Contact(email="contact@snippets.local"),    # noqa: E800
        #   license=openapi.License(name="BSD License"),    # noqa: E800
    ),
    public=True,
    #    permission_classes=[permissions.AllowAny],)    # noqa: E800
)



urlpatterns = [
    path("conmander/", admin.site.urls),
    path("api/signin/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path(
        "api/docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),

]
