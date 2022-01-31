from django.db import models


class MaterialClassEnum(models.TextChoices):
    PLASTIC = "Plastik",
    WOOD = "Holz",
    METAL = "Metall",
    TEXTILE = "Textil"


class MaterialPropertyEnum(models.TextChoices):
    # HEAT_RESISTENCE = "Hitzbeständigkeit",
    TENSILE_STRENGTH = "Zugfestigkeit",
    BREAKING_STRENGTH = "Dehngrenze",
    DENSITY = "Dichte",
    FRACTURE_STRAIN = "Bruchdehnung"
    HARDNESS = "Härte"
    # MOISTURE_RESISTENCE = "Feuchtigkeitsresistenz",
    # SURFACE_TEXTURE = "Oberflächenbeschaffenheit"


class SustainabilityPropertyEnum(models.TextChoices):
    CO2_CONSUMPTION = "CO2 Verbrauch",
    WATER_CONSUMPTION = "Wasserverbrauch",
    ENERGY_CONSUMPTION = "Energieverbrauch",
    RECYCLABILTY = "Recyclingfähigkeit",