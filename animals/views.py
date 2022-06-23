from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Animal
from .serializers import AnimalsSerializer

# Create your views here.

class AnimalView(APIView):

    def get(self, request):
        animals = Animal.objects.all()

        serializer = AnimalsSerializer(animals, many=True)

        return Response(serializer.data)

    def post(self,request):
        serializer = AnimalsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleAnimalView(APIView):

    def get(self, request, animal_id):
        try:
            animal = Animal.objects.get(id=animal_id)
        except Animal.DoesNotExist:
            return Response({"message": "Animal not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = AnimalsSerializer(animal)

        return Response(serializer.data, status=status.HTTP_200_OK)
        
    def patch(self, request, animal_id):
        animal = get_object_or_404(Animal, id=animal_id)
        
        if 'sex' in request.data:
            return Response({"message": "You can not update sex property"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        if 'group' in request.data:
            return Response({"message": "You can not update group property"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        serializer = AnimalsSerializer(animal, request.data, partial=True)

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data)

    def delete(self,request,animal_id):
        get_object_or_404(Animal, id=animal_id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
