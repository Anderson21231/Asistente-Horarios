from django.http import request
from django.shortcuts import render
from asistenteHorarios.models import Instructores, Contratacion
import csv, io
from django.contrib import messages
from datetime import date, datetime

def listaInstructores(request):
    template = "listarInstructor.html"
   
    return render(request, template) 

