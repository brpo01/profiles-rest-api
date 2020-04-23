# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import serializers
from rest_framework import status

# Create your views here.

class HelloApiView(APIView):
    
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):

        an_apiview = [
            'Uses http methods as functions (get, put, post,patch , delete)',
            'It is similar to a traditional django view',
            'Gives you control over your logic',
            'is mapped manually to your URLs'
        ]
        
        return Response({
            'message':'Hello!',
            'an apiview': an_apiview,
        })
        
    def post(self, request):
        
        serializer = serializers.HelloSerializer(data=request.data)
        
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            
            return Response({
                'message':message,
            })
            
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        """ Handles updating an object """
        return Response({
            'method':'put'
        })
        
    def patch(self, request, pk=None):
        """ only updates fields provided in request """
        
        return Response({
            'method':'patch'
        })
        
    def delete(self, request, pk=None):
        """ deletes an object  """
        
        return Response({
            'method':'delete'
        })