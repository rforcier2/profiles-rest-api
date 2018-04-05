from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloApiView(APIView):
    """EXAMPLE API View."""

    def get(self, request, format=None):
        """Returns a list of APIView features."""

        an_apiview = [
            'Uses HTTP Methods as function (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most control over your logic',
            'Is mapped manually to URLs'
        ]
        example_section = [
            'this is an API example',
            'I totally know what I am doing',
        ]

        return Response({'message' : 'Hello!', 'an_apiview': an_apiview, 'Example Section': example_section})
