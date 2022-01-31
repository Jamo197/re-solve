from rest_framework import serializers

from materials.models import Article, Property, Material, SustainabilityProperty


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        exclude = ("material",)


class SustainabilityPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = SustainabilityProperty
        exclude = ("material",)


class MaterialSerializer(serializers.ModelSerializer):
    # TODO: required=False
    properties = PropertySerializer(many=True)
    sustainability_properties = SustainabilityPropertySerializer(many=True)

    class Meta:
        model = Material
        fields = "__all__"
    
    # TODO: check if properties_data && sustain_properties_data exists
    def create(self, validated_data):
        properties_data = validated_data.pop('properties')
        sustain_properties_data = validated_data.pop('sustainability_properties')

        material = Material.objects.create(**validated_data)

        for property_data in properties_data:
            Property.objects.create(material=material, **property_data)
        for sustain_property_data in sustain_properties_data:
            SustainabilityProperty.objects.create(material=material, **sustain_property_data)
        
        return material 

    # TODO: SAME!!! check if properties_data && sustain_properties_data exists
    def update(self, instance, validated_data):
        properties_data = validated_data.pop('properties')
        properties = (instance.properties).all()
        properties = list(properties)
        sustain_properties_data = validated_data.pop('sustainability_properties')
        sustain_properties = (instance.sustainability_properties).all()
        sustain_properties = list(sustain_properties)

        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.material_class = validated_data.get('material_class', instance.material_class)
        instance.save()

        for property_data in properties_data:
            prop = properties.pop(0)
            prop.property_name = property_data.get('property_name', prop.property_name)
            prop.value = property_data.get('value', prop.value)
            prop.unit = property_data.get('unit', prop.unit)
            prop.save()
        for sustain_property_data in sustain_properties_data:
            sustain_prop = sustain_properties.pop(0)
            sustain_prop.property_name = sustain_property_data.get('property_name', sustain_prop.property_name)
            sustain_prop.value = sustain_property_data.get('value', sustain_prop.value)
            sustain_prop.unit = sustain_property_data.get('unit', sustain_prop.unit)
            sustain_prop.save()
        return instance


class ArticleSerializer(serializers.ModelSerializer):
    material = MaterialSerializer(many=False, read_only=True)
    ecological_index = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"
    
    def get_ecological_index(self, instance):
        return instance.material.ecological_index