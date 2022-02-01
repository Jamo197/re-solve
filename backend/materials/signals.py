from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .enums import SustainabilityPropertyEnum
from .models import Material, SustainabilityProperty


def get_max_water_consumption(new_val):
    properties = SustainabilityProperty.objects.all()
    max_water_consumption = max(mat_prop.value for mat_prop in properties if mat_prop.property_name == SustainabilityPropertyEnum.WATER_CONSUMPTION)

    return max_water_consumption if max_water_consumption > new_val else new_val


# TODO: Wenn man den höchsten Wert runter setzt, wird er im nächsten step trotzdem noch als höchster Wert behandelt
def get_max_energy_consumption(new_val):
    properties = SustainabilityProperty.objects.all()
    max_energy_consumption = max(mat_prop.value for mat_prop in properties if mat_prop.property_name == SustainabilityPropertyEnum.ENERGY_CONSUMPTION)
    
    return max_energy_consumption if max_energy_consumption > new_val else new_val


def get_max_co2_consumption(new_val):
    properties = SustainabilityProperty.objects.all()
    max_co2_consumption = max(mat_prop.value for mat_prop in properties if mat_prop.property_name == SustainabilityPropertyEnum.CO2_CONSUMPTION)
    
    return max_co2_consumption if max_co2_consumption > new_val else new_val

def calculate_ecological_index(instance):
    co2_consumption = 1.0
    recyclability = 1.0
    energy_consumption = 1.0
    water_consumption = 1.0
    for inst_prop in instance.sustainability_properties.all():
        if inst_prop.property_name == SustainabilityPropertyEnum.CO2_CONSUMPTION:
            co2_consumption = (100 / get_max_co2_consumption(inst_prop.value) * inst_prop.value) * 0.05
        elif inst_prop.property_name == SustainabilityPropertyEnum.RECYCLABILTY:
            recyclability = 5 - (inst_prop.value * 0.05)
        elif inst_prop.property_name == SustainabilityPropertyEnum.ENERGY_CONSUMPTION:
            energy_consumption = (100 / get_max_energy_consumption(inst_prop.value) * inst_prop.value) * 0.05
        elif inst_prop.property_name == SustainabilityPropertyEnum.WATER_CONSUMPTION:
            water_consumption = (100 / get_max_water_consumption(inst_prop.value) * inst_prop.value) * 0.05

    return (co2_consumption + recyclability + energy_consumption + water_consumption) / 4

# @receiver(pre_save, sender=SustainabilityProperty)
def calc_eco_score(sender, instance, *args, **kwargs):
    if instance:
        # Berechnung CO2 Verbrauch
        if instance.property_name == SustainabilityPropertyEnum.CO2_CONSUMPTION:
            instance.eco_score = (100 / get_max_co2_consumption(instance.value) * instance.value) * 0.05
        # Berechnung Recyclingfähigkeit
        elif instance.property_name == SustainabilityPropertyEnum.RECYCLABILTY:
            instance.eco_score = 5 - (instance.value * 0.05)
        # Berechnung Energieverbrauch
        elif instance.property_name == SustainabilityPropertyEnum.ENERGY_CONSUMPTION:
            instance.eco_score = (100 / get_max_energy_consumption(instance.value) * instance.value) * 0.05
        # Berechnung Wasserverbrauch
        elif instance.property_name == SustainabilityPropertyEnum.WATER_CONSUMPTION:
            instance.eco_score = (100 / get_max_water_consumption(instance.value) * instance.value) * 0.05


# @receiver(post_save, sender=SustainabilityProperty)
def calc_materials_eco_index(sender, instance, *args, **kwargs):
    materials = Material.objects.all()

    for material in materials:
        if material.sustainability_properties.count() > 0:
            counter = 0
            eco_score = 0
            for prop in material.sustainability_properties.all():
                counter += 1
                eco_score += prop.eco_score
            material.ecological_index = eco_score / counter
        material.save()
