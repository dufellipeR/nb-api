from .models import Character
from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name', 'desc', 'clan', 'age', 'photo', 'ninjutsu', 'taijutsu',
                  'genjutsu', 'intelligence', 'strength', 'speed', 'stamina', 'handseals', 'ninjarank', 'rarity', 'baseoverall', 'bonus', 'overall']
