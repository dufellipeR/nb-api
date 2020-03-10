from .models import Character
from rest_framework import viewsets
from .serializers import CharacterSerializer
from django.http import JsonResponse


class CharacterViewSet(viewsets.ModelViewSet):

    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

    def create(self, request):
        print(request.data)

        data = request.data

        total = (int(data['ninjutsu']) + int(data['taijutsu']) + int(data['genjutsu']) + int(
            data['intelligence']) + int(data['strength']) + int(data['speed']) + int(data['stamina']) + int(data['handseals']))

        baseoverall = round(total / 8, 0)
        print(total, baseoverall)

        bonus = 0

        if data['bonus'] == '':
            bonus = 0
        else:
            bonus = data['bonus']

        overall = 0

        if data['overall'] == '':
            overall = 0
        else:
            overall = data['overall']

        c = Character()
        c.name = data['name']
        c.desc = data['desc']
        c.age = data['age']
        c.clan = data['clan']
        c.ninjutsu = data['ninjutsu']
        c.taijutsu = data['taijutsu']
        c.genjutsu = data['genjutsu']
        c.intelligence = data['intelligence']
        c.strength = data['strength']
        c.speed = data['speed']
        c.stamina = data['stamina']
        c.handseals = data['handseals']
        c.ninjarank = data['ninjarank']
        c.rarity = data['rarity']
        c.bonus = bonus
        c.baseoverall = baseoverall
        c.overall = overall
        c.save()

        return JsonResponse({'message': 'Ninja Created'})
