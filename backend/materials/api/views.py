from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from materials.enums import SustainabilityPropertyEnum, MaterialPropertyEnum

from materials.models import Material, Article, Property, SustainabilityProperty
from materials.api.serializers import (MaterialSerializer, ArticleSerializer,
                                       PropertySerializer, SustainabilityPropertySerializer)


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class PropertyCreateAPIView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def perform_create(self, serializer):
        material_pk = self.kwargs.get("material_pk")
        material = get_object_or_404(Material, pk=material_pk)
        serializer.save(material=material)


class PropertyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class SustainabilityPropertyCreateAPIView(generics.CreateAPIView):
    queryset = SustainabilityProperty.objects.all()
    serializer_class = SustainabilityPropertySerializer

    def perform_create(self, serializer):
        material_pk = self.kwargs.get("material_pk")
        material = get_object_or_404(Material, pk=material_pk)
        serializer.save(material=material)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class FilterArticleAPIView(generics.ListAPIView):
    serializer_class = ArticleSerializer
    
    def get_best_match_by_material_properties(self, queryset, filter_paramters):
        for key, value in filter_paramters.items():
            if value is not None:
                if key == "article_depth":
                    queryset = queryset.filter(depth=value)
                if key == "article_length":
                    queryset = queryset.filter(length=value)
                if key == "article_width":
                    queryset = queryset.filter(length=value)
                # Materialeigenschaften
                if key == "tensile_strength":
                    queryset = queryset.filter(material__properties__property_name=MaterialPropertyEnum.TENSILE_STRENGTH,
                                               material__properties__value=value)
                if key == "breaking_strength":
                    queryset = queryset.filter(material__properties__property_name=MaterialPropertyEnum.BREAKING_STRENGTH,
                                               material__properties__value=value)
                if key == "density":
                    queryset = queryset.filter(material__properties__property_name=MaterialPropertyEnum.DENSITY,
                                               material__properties__value=value)
                if key == "fracture_strain":
                    queryset = queryset.filter(material__properties__property_name=MaterialPropertyEnum.FRACTURE_STRAIN,
                                               material__properties__value=value)
                if key == "hardness":
                    queryset = queryset.filter(material__properties__property_name=MaterialPropertyEnum.HARDNESS,
                                               material__properties__value=value)
        return queryset.order_by('-material__ecological_index')

    def get_queryset(self):
        # TODO: einzelne Objekte selber filtern, erst Eigenschaften, dann Materialien, dann die gewünschten Artikel anzeigen
        queryset = Article.objects.all()
        filter_paramters = {}
        filter_paramters["article_name"] = self.request.GET.get('article_name', None)
        filter_paramters["article_depth"] = self.request.GET.get('article_depth', None)
        filter_paramters["article_length"] = self.request.GET.get('article_length', None)
        filter_paramters["article_width"] = self.request.GET.get('article_width', None)
        filter_paramters["material_class"] = self.request.GET.get('material_class', None)

        # Material Eigenschaften
        filter_paramters["tensile_strength"] = self.request.GET.get('tensile_strength', None)
        filter_paramters["breaking_strength"] = self.request.GET.get('breaking_strength', None)
        filter_paramters["density"] = self.request.GET.get('density', None)
        filter_paramters["fracture_strain"] = self.request.GET.get('fracture_strain', None)
        filter_paramters["hardness"] = self.request.GET.get('hardness', None)

        for key, value in filter_paramters.items():
            if value is not None:
                if key == "article_name":
                    queryset = queryset.filter(name__contains=value)
                if key == "material_class":
                    queryset = queryset.filter(material__material_class=value)
                if key == "article_depth":
                    max_value = float(value) * 1.2
                    queryset = queryset.filter(depth__gte=value, depth__lte=max_value)
                if key == "article_length":
                    queryset = queryset.filter(length__gte=value)
                if key == "article_width":
                    queryset = queryset.filter(length__gte=value)
                # Materialeigenschaften
                if key == "tensile_strength":
                    min_value = float(value) * 0.7
                    max_value = float(value) * 1.3
                    queryset = queryset.filter(material__properties__property_name=MaterialPropertyEnum.TENSILE_STRENGTH,
                                               material__properties__value__gte=min_value,
                                               material__properties__value__lte=max_value)
                if key == "breaking_strength":
                    min_value = float(value) * 0.7
                    max_value = float(value) * 1.3
                    queryset = queryset.filter(material__properties__property_name=MaterialPropertyEnum.BREAKING_STRENGTH,
                                               material__properties__value__gte=min_value,
                                               material__properties__value__lte=max_value)
                if key == "density":
                    min_value = float(value) * 0.7
                    max_value = float(value) * 1.3
                    queryset = queryset.filter(material__properties__property_name=MaterialPropertyEnum.DENSITY,
                                               material__properties__value__gte=min_value,
                                               material__properties__value__lte=max_value)
                if key == "fracture_strain":
                    min_value = float(value) * 0.7
                    max_value = float(value) * 1.3
                    queryset = queryset.filter(material__properties__property_name=MaterialPropertyEnum.FRACTURE_STRAIN,
                                               material__properties__value__gte=min_value,
                                               material__properties__value__lte=max_value)
                if key == "hardness":
                    min_value = float(value) * 0.7
                    max_value = float(value) * 1.3
                    queryset = queryset.filter(material__properties__property_name=MaterialPropertyEnum.HARDNESS,
                                               material__properties__value__gte=min_value,
                                               material__properties__value__lte=max_value)


        # TODO: das genaueste Ergebnis muss nach vorne und dann erst nach eco index
        best_matches = self.get_best_match_by_material_properties(queryset, filter_paramters)
        queryset = list(queryset.order_by('material__ecological_index'))
        if len(best_matches) > 0:
            for best_match in best_matches: 
                queryset.remove(best_match)
                queryset.insert(0, best_match)
        return queryset