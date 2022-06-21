from rest_framework import serializers

class CharacteristicsSerializer(serializers.Serializer):
    name = serializers.CharField()