from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255, blank=True, null=True)
    clan = models.CharField(max_length=64, blank=True, null=True)
    age = models.CharField(max_length=64, blank=True, null=True)
    photo = models.ImageField(upload_to='media', blank=True, null=True)
    ninjutsu = models.IntegerField(blank=True, null=True)
    taijutsu = models.IntegerField(blank=True, null=True)
    genjutsu = models.IntegerField(blank=True, null=True)
    intelligence = models.IntegerField(blank=True, null=True)
    strength = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    stamina = models.IntegerField(blank=True, null=True)
    handseals = models.IntegerField(blank=True, null=True)
    ninjarank = models.CharField(max_length=64, blank=True, null=True)
    rarity = models.CharField(max_length=155, blank=True, null=True)
    bonus = models.DecimalField(
        max_digits=155, decimal_places=2, blank=True, null=True)
    baseoverall = models.IntegerField(
        blank=True, null=True)
    overall = models.DecimalField(
        max_digits=155, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name
