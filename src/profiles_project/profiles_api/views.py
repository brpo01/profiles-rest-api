# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    
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