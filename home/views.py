from django.shortcuts import render
from home.models import Factory
from home.api_file.serializer import FactorySerializer
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class Factory_view (APIView):
    

    def get (self , request):
        factory = Factory.objects.all ()
        serializer = FactorySerializer (factory , many=True)
        return Response (serializer.data)
    
    def post (self , request):
        serializer = FactorySerializer (data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors)
        
class Factory_detail (APIView):
    
    def get (self , request , pk):
        try :
            factory = Factory.objects.get (pk = pk)
        except:
            return Response ({"Error" : 'Factory not Found'} , status=status.HTTP_404_NOT_FOUND)
        serializer = FactorySerializer (factory)
        return Response (serializer.data)
    
    def post (self, request , pk):
        factory = Factory.objects.get (pk = pk)
        serializer = FactorySerializer (factory , data=request.data)
        if serializer.is_valid ():
            serializer.save ()
            return Response (serializer.data)
        else :
            return Response (serializer.errors)
        
    def delete (self , request , pk):
        factory = Factory.objects.get (pk = pk)
        factory.delete ()
        return Response (status=status.HTTP_204_NO_CONTENT)
        
 
        
        
    
