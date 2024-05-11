from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
# Create your views here.

@api_view(['GET'])
def retrieve(request):
    query_set=Student.objects.all()
    serializer_class=StudentSerializer(query_set,many=True)
    return Response(serializer_class.data)

@api_view(['POST'])
def create(request):
    query_set=Student.objects.all()
    serializer_class=StudentSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
    return Response(serializer_class.data)

@api_view(['POST'])
def update(request,id):
    query_set=Student.objects.get(id=id)
    serializer_class=StudentSerializer(instance=query_set,data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
    return Response(serializer_class.data)


@api_view(['DELETE'])
def delete(request,id):
    query_set=Student.objects.get(id=id)
    query_set.delete()
    return Response('data deleted')