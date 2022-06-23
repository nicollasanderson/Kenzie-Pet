from rest_framework import serializers
from groups.serializers import GroupsSerializer
from characteristics.serializers import CharacteristicsSerializer
from animals.models import Animal
from groups.models import Group
from characteristics.models import Characteristic

class AnimalsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    age = serializers.FloatField()
    weight = serializers.FloatField()
    sex = serializers.CharField()
    group = GroupsSerializer()
    characteristics = CharacteristicsSerializer(many=True)

    def create(self,validated_data):

        group = Group.objects.get_or_create(**validated_data["group"])[0]
        
        listt = validated_data['characteristics']

        validated_data.pop('group')
        validated_data.pop('characteristics')

        animal = Animal.objects.create(**validated_data)

        for value in listt:
            caract = Characteristic.objects.get_or_create(**value)[0]
            animal.characteristics.add(caract)

        animal.group_id = group.id
        
        animal.save()

        return animal

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.weight = validated_data.get('weight', instance.weight)

        try:
            for value in validated_data['characteristics']:
                caract = Characteristic.objects.get_or_create(**value)[0]
                instance.characteristics.add(caract)
        except:
            pass

        instance.save()
        return instance