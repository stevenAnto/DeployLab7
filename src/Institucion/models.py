from operator import mod
from django.db import models

# Create your models here.
class Tutor(models.Model):
    codigoTutor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoDocumento = models.CharField(max_length=50)
    numDocumento = models.CharField(max_length=15)

    def nombre_completo(self):
        return "{}, {}".format(self.apellidos, self.nombres)
    def __str__(self):
        return self.nombre_completo()

class Alumno(models.Model):
    codigoAlumno = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50, verbose_name='Nombres')
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    tipoDocumento = models.CharField(max_length=50)
    numDocumento = models.CharField(max_length=15)
    fechaNacimiento = models.DateField()
    codigoTutor = models.ForeignKey(Tutor, related_name='fk_alumno', on_delete=models.CASCADE)

    def nombre_completo(self):
        return "{}, {}".format(self.apellidos, self.nombres)
    def __str__(self):
        return self.nombre_completo()

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoUsuario = models.CharField(max_length=100)
    def nombre_completo(self):
        return "{}, {}".format(self.apellidos, self.nombres)
    def __str__(self):
        return self.nombre_completo()


class Profesor(models.Model):
    codigoProfesor = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    tipoDocumento = models.CharField(max_length=50)
    numDocumento = models.CharField(max_length=15)
    def nombre_completo(self):
        return "{}, {}".format(self.apellidos, self.nombres)
    def __str__(self):
        return self.nombre_completo()

class Cursos(models.Model):
    codigoCurso = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits = 7, decimal_places = 2)
    fk_codigoProfesor = models.ForeignKey(Profesor, related_name='fk_profesor',blank=True, on_delete=models.CASCADE)
    fechaInicio = models.DateField()
    fechaFin = models.DateField()

    def __str__(self):
        return self.nombre

class Matriculas(models.Model):
    codigoRegistro = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500)
    codigoAlumno = models.ForeignKey(Alumno, related_name='fk_alumno', on_delete=models.CASCADE)
    codigoCurso = models.ForeignKey(Cursos, related_name='fk_cursos', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits = 7, decimal_places = 2)

class Honorarios(models.Model):
    codigoHonorario = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=500)
    codigoProfesor = models.ForeignKey(Profesor, related_name='fk_profesor_h', on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits = 7, decimal_places = 2)
    
    def detalle(self):
        return "{} - {}".format(self.codigoProfesor, self.monto)
    def __str__(self):
        return self.detalle()
