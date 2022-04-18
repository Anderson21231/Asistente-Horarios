from django.http import request
from django.shortcuts import render
from asistenteHorarios.models import Instructores, Contratacion
import csv, io
from django.contrib import messages
from datetime import date, datetime

def cargarInstructor(request):
    template = "cargarInstructor.html"
   
    return render(request, template) 


