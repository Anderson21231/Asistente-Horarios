from django.db import models

class Catalogo_Perfiles(models.Model):
    Perfil = models.CharField(max_length=30)

class Instructores(models.Model):
    NumeroDocumento = models.CharField(max_length=20)
    TipoDocumento = models.CharField(max_length=2)  
    Nombre = models.CharField(max_length=50)
    Apellido = models.CharField(max_length=50)
    id_Perfiles = models.ForeignKey(Catalogo_Perfiles, null=True, on_delete=models.CASCADE)

class Contratacion(models.Model):
    Fecha_Inicio = models.DateField()  # hay que corregir el tipo de dato a "DateField"
    Fecha_Fin = models.DateField() # hay que corregir el tipo de dato a "DateField"
    Supervisora = models.CharField(max_length=100)
    id_Instructor = models.ForeignKey(Instructores, null=True, on_delete=models.CASCADE)
    horasMensualFormacion = models.IntegerField(null=True)

