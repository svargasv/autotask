from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .logic import create
from rest_framework.exceptions import MethodNotAllowed
from django.core.exceptions import ValidationError
from django.http import HttpResponse
import json
# Create your views here.
@api_view(['POST'])
def viewCreateCalendar(request):
    if request.method == 'POST':
        try:
            events = create.createCalendar()
            for event in events:
                #ACA SE MANDA A GOOGLE CALENDAR
                pass
            return Response('Cargado exitosamente', status=status.HTTP_200_OK)
        
        except ValidationError:
            return Response('Error en la validación del archivo',status=status.HTTP_400_BAD_REQUEST)
    else: 
        raise   MethodNotAllowed()

def viewTest(request):
    return HttpResponse('Hola')
