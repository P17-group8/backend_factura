"""factura_ms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, re_path

from app_factura.views import PlazaCreateView, PlazaDetailView, PlazaUpdateView, PlazaDeleteView, AvailablePlazas
from app_factura.views import FacturaCreateView, FacturaDetailView, FacturaUpdateView, FacturaDeleteView, CheckOutView 

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="MS-Factura - Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/',                 admin.site.urls),
    path('admin/#/',               admin.site.urls),    
    path('plaza/create/',          PlazaCreateView.as_view()),
    path('plaza/<int:pk>/',        PlazaDetailView.as_view()),
    path('plaza/update/<int:pk>/', PlazaUpdateView.as_view()),
    path('plaza/delete/<int:pk>/', PlazaDeleteView.as_view()),
    path('plaza/available/',       AvailablePlazas.as_view()),

    path('factura/create/',          FacturaCreateView.as_view()),
    path('factura/<int:pk>/',        FacturaDetailView.as_view()),
    path('factura/update/<int:pk>/', FacturaUpdateView.as_view()),
    path('factura/delete/<int:pk>/', FacturaDeleteView.as_view()),
    path('factura/checkout/<int:pk>/', CheckOutView.as_view()),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


