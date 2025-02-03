from django.http import JsonResponse
from .models import Ans
from .serializer import AnsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET','POST'])

def Ans_list (request,format=None):

    if request.method == 'GET':


        #Get all the drinks
        #Serializer them 
        #return JSON
        Answer= Ans.objects.all()
        serializer= AnsSerializer(Answer, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer= AnsSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# @api_view(['GET','PUT', 'DELETE'])    
# def drink_detail(request, id, format=None):

#     try:
#         drink= Drink.objects.get(pk=id)
#     except Drink.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = DrinkSerializer(drink)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         serializer = DrinkSerializer(drink, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         drink.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

     