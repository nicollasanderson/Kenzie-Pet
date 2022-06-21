from rest_framework import serializers

class GroupsSerializer(serializers.Serializer):
    name = serializers.CharField()
    scientific_name = serializers.CharField()