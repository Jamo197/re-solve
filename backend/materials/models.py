from django.db import models

from .enums import MaterialClassEnum, MaterialPropertyEnum, SustainabilityPropertyEnum


class Material(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120, blank=True, null=True)
    material_class = models.CharField(choices=MaterialClassEnum.choices, max_length=20)
    # Wenn e_index < 0, keine Werte angegeben
    # TODO: Maybe back to Decimalfield
    ecological_index = models.FloatField(default=-1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}, {self.description}"


class Property(models.Model):

    property_name = models.CharField(choices=MaterialPropertyEnum.choices, max_length=25)
    value = models.FloatField(default=0)
    # TODO: Make to Choice Field
    unit = models.CharField(max_length=60)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="properties")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.property_name

    class Meta:
        verbose_name_plural = "properties"
        
class SustainabilityProperty(models.Model):

    property_name = models.CharField(choices=SustainabilityPropertyEnum.choices, max_length=60)
    value = models.FloatField(default=0)
    # TODO: Make to Choice Field
    unit = models.CharField(max_length=60)
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name="sustainability_properties")
    # TODO: Wird nach den max und min Werten der anderen Materialien bewertet
    eco_score = models.DecimalField(default=0, max_digits=4, decimal_places=3)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.property_name

    class Meta:
        verbose_name_plural = "sustainability_properties"

class Article(models.Model):

    name = models.CharField(max_length=30)
    description = models.CharField(max_length=120, blank=True, null=True)

    # TODO: Implementieren, wenn User bzw. Lieferant drin ist
    # supplier_id = LiefererId
    
    material = models.ForeignKey(Material, on_delete=models.CASCADE)

    depth = models.FloatField(default=0)
    length = models.FloatField(default=0)
    width = models.FloatField(default=0)

    price = models.FloatField(default=0)
    replaceability_index = models.PositiveIntegerField(default=0)

    quantity_in_stock = models.PositiveIntegerField(default=0)
    # in_stock = True if quantity_in_stock > 0
    in_stock = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
