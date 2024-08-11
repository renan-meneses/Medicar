
from django.contrib import admin
from drf_yasg import openapi
from rest_framework import routers
from django.urls import path, include
from drf_yasg.views import get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import AllowAny
from controller.user.views import UserViewSet
from controller.clinic.views import (
    SpecialtyViewSet, DoctorViewSet,
    AgendaViewSet, MedicalAppointmentViewSet
)

schema_view = get_schema_view(
    openapi.Info(
        title="Medica API",
        default_version="v1",
        description="Sistema voltado a gerenciamento de clinica medica",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="suport@medicar.com"),    # noqa: E800
        license=openapi.License(name="BSD License"),    # noqa: E800
    ),
    public=True,
    permission_classes=(AllowAny,), 

)

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('especialidades', SpecialtyViewSet)
router.register('medicos', DoctorViewSet)
router.register('agendas', AgendaViewSet)
router.register('consultas', MedicalAppointmentViewSet)

urlpatterns = [
    path("controller/", admin.site.urls),
    path("api/signin/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path('', include(router.urls)),


]
