from tokenize import group
from rest_framework import serializers
from groups.serializers import GroupsSerializer
from characteristics.serializers import CharacteristicsSerializer
from animals.models import Animal
from groups.models import Group
from characteristics.models import Characteristic

class AnimalsSerializer(serializers.Serializer):
    name = serializers.CharField()
    age = serializers.IntegerField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    group = GroupsSerializer()
    characteristics = CharacteristicsSerializer(many=True)

    # GroupsSerializer()
    # CharacteristicsSerializer(many=True)
    

    def create(self,validated_data):

        group = Group.objects.get_or_create(**validated_data["group"])[0]
        
        listt = validated_data['characteristics']

        validated_data.pop('group')
        validated_data.pop('characteristics')

        animal = Animal.objects.create(**validated_data)

        for value in listt:
            caract = Characteristic.objects.get_or_create(**value)[0]
            animal.characteristics.add(caract)

        print(animal.__dict__)
        animal.group_id = group.id

        animal.save()
        
        print(group)
        return animal.__dict__



