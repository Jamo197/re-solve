from django.urls import include, path
from rest_framework.routers import DefaultRouter

from materials.api.views import (MaterialViewSet,
                                 PropertyCreateAPIView, 
                                 PropertyDetailAPIView,
                                 SustainabilityPropertyCreateAPIView,
                                 ArticleViewSet,
                                 FilterArticleAPIView)

router = DefaultRouter()
router.register(r'materials', MaterialViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
     path("", include(router.urls)), 
     path("materials/<int:material_pk>/property/", 
          PropertyCreateAPIView.as_view(), 
          name="material-property"),

     path("properties/<int:pk>/", 
          PropertyDetailAPIView.as_view(), 
          name="property-detail"),

     path("materials/<int:material_pk>/sustainability_property/", 
          SustainabilityPropertyCreateAPIView.as_view(), 
          name="material-sustainability"),

     path("filter/articles/", 
          FilterArticleAPIView.as_view(), 
          name="filter-article"),
]