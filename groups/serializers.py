from rest_framework import serializers

class GroupsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    scientific_name = serializers.CharField()