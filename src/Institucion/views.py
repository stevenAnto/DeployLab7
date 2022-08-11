from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Institucion.models import Alumno, Admin, Honorarios, Matriculas, Profesor, Cursos, Tutor
from Institucion.serializers import AlumnoSerializer, AdminSerializer, AdminsGetSerializer, HonorariosSerializer, MatriculaSerializer, ProfesorSerializer, CursosSerializer, TutorSerializer
from rest_framework import viewsets
# Create your views here.


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursosSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matriculas.objects.all()
    serializer_class = MatriculaSerializer

class HonorariosViewSet(viewsets.ModelViewSet):
    queryset = Honorarios.objects.all()
    serializer_class = HonorariosSerializer

class TutorViewSet(viewsets.ModelViewSet):
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer

# #ALUMNOS
# @csrf_exempt
# def alumnoApi(request, codigoAlumno=0):
#     if request.method == 'GET':
#         alumnos = Alumno.objects.all()
#         alumnos_serializer = AlumnoSerializer(alumnos, many=True)
#         return JsonResponse(alumnos_serializer.data, safe=False)
#     elif request.method == 'POST':
#         alumno_data = JSONParser().parse(request)
#         alumno_serializer = AlumnoSerializer(data = alumno_data)
#         if alumno_serializer.is_valid():
#             alumno_serializer.save()
#             return JsonResponse("Alumno registrado exitosamente!!", safe=False)
#         return JsonResponse("Error al registrar alumno", safe=False)
#     elif request.method == 'PUT':
#         alumno_data = JSONParser().parse(request)
#         alumno_before = Alumno.objects.get(codigoAlumno = alumno_data['codigoAlumno'])
#         alumno_serializer = AlumnoSerializer(alumno_before, data = alumno_data)
#         if alumno_serializer.is_valid():
#             alumno_serializer.save()
#             return JsonResponse("Datos del alumno actualizado exitosamente!!", safe=False)
#         return JsonResponse("Error al actualizar los datos del alumno", safe=False)
#     elif request.method == 'DELETE':
#         alumno = Alumno.objects.get(codigoAlumno=codigoAlumno)
#         alumno.delete()
#         return JsonResponse("Alumno eliminado exitosamente!!", safe=False)

# #USUARIOS ADMIN
# @csrf_exempt
# def adminApi(request, id=0):
#     if request.method == 'GET':
#         admins = Admin.objects.all()
#         admin_serializer = AdminsGetSerializer(admins, many=True)
#         return JsonResponse(admin_serializer.data, safe=False)
#     elif request.method == 'POST':
#         admin_data = JSONParser().parse(request)
#         admin_serializer = AdminSerializer(data = admin_data)
#         if admin_serializer.is_valid():
#             admin_serializer.save()
#             return JsonResponse("Usuario registrado exitosamente!!", safe=False)
#         return JsonResponse("Error al registrar el usuario", safe=False)
#     elif request.method == 'PUT':
#         admin_data = JSONParser().parse(request)
#         admin_before = Admin.objects.get(id = admin_data['id'])
#         admin_serializer = AdminSerializer(admin_before, data = admin_data)
#         if admin_serializer.is_valid():
#             admin_serializer.save()
#             return JsonResponse("Datos del usuario actualizado exitosamente!!", safe=False)
#         return JsonResponse("Error al actualizar los datos del usuario", safe=False)
#     elif request.method == 'DELETE':
#         admin = Admin.objects.get(id=id)
#         admin.delete()
#         return JsonResponse("Usuario eliminado exitosamente!!", safe=False)

# #PROFESORES
# @csrf_exempt
# def profesorApi(request, codigoProfesor=0):
#     if request.method == 'GET':
#         profesores = Profesor.objects.all()
#         profesor_serializer = ProfesorSerializer(profesores, many=True)
#         return JsonResponse(profesor_serializer.data, safe=False)
#     elif request.method == 'POST':
#         profesor_data = JSONParser().parse(request)
#         profesor_serializer = ProfesorSerializer(data = profesor_data)
#         if profesor_serializer.is_valid():
#             profesor_serializer.save()
#             return JsonResponse("Profesor registrado exitosamente!!", safe=False)
#         return JsonResponse("Error al registrar el profesor", safe=False)
#     elif request.method == 'PUT':
#         profesor_data = JSONParser().parse(request)
#         profesor_before = Profesor.objects.get(codigoProfesor = profesor_data['codigoProfesor'])
#         profesor_serializer = ProfesorSerializer(profesor_before, data = profesor_data)
#         if profesor_serializer.is_valid():
#             profesor_serializer.save()
#             return JsonResponse("Datos del profesor actualizado exitosamente!!", safe=False)
#         return JsonResponse("Error al actualizar los datos del profesor", safe=False)
#     elif request.method == 'DELETE':
#         profesor = Profesor.objects.get(codigoProfesor=codigoProfesor)
#         profesor.delete()
#         return JsonResponse("Profesor eliminado exitosamente!!", safe=False)

# #CURSOS
# @csrf_exempt
# def cursosApi(request, codigoCurso=0):
#     if request.method == 'GET':
#         cursos = Cursos.objects.all()
#         curso_serializer = CursosSerializer(cursos, many=True)
#         return JsonResponse(curso_serializer.data, safe=False)
#     elif request.method == 'POST':
#         curso_data = JSONParser().parse(request)
#         curso_serializer = CursosSerializer(data = curso_data, many=True)
#         print(curso_serializer);
#         if curso_serializer.is_valid():
#             curso_serializer.save()
#             return JsonResponse("Curso agregado exitosamente!!", safe=False)
#         return JsonResponse("Error al registrar el curso")
#     elif request.method == 'PUT':
#         curso_data = JSONParser().parse(request)
#         curso_before = Cursos.objects.get(codigoCurso = curso_data['codigoCurso'])
#         curso_serializer = CursosSerializer(curso_before, data = curso_data)
#         if curso_serializer.is_valid():
#             curso_serializer.save()
#             return JsonResponse("Datos del curso actualizado exitosamente!!", safe=False)
#         return JsonResponse("Error al actualizar los datos del profesor", safe=False)
#     elif request.method == 'DELETE':
#         curso = Cursos.objects.get(codigoCurso=codigoCurso)
#         curso.delete()
#         return JsonResponse("Curso eliminado exitosamente!!", safe=False)

@csrf_exempt
def detailApi(request):
    if request.method == 'GET':
        
        list_precios_cursos = Cursos.objects.values_list('precio', flat=True)
        list_honorarios_profesores = Honorarios.objects.values_list('monto', flat=True)
        resp_data = {'cantidadCursos': len(Cursos.objects.all()), 
                     'cantidadAlumnos': len(Alumno.objects.all()),
                     'cantidadPadres': len(Tutor.objects.all()),
                     'cantidadProfesores': len(Profesor.objects.all()),
                     'montoTotalCursos': sum(list_precios_cursos),
                     'montoTotalHonorariosProfesores': sum(list_honorarios_profesores)
                     }
        return JsonResponse(resp_data)

@csrf_exempt
def loginAdminApi(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            result = Admin.objects.get(usuario=data['usuario'], password=data['password'])
            res = AdminSerializer(result, many=False)
            nombre = res.data['nombres']
            return JsonResponse("Bienvenido "+nombre, safe=False)
        except Admin.DoesNotExist:
            return JsonResponse("Usuario invalido", safe=False)
        #resp_data = {'cantidadCursos': 1 }

@csrf_exempt
def misCursosApi(request):
    if request.method == 'GET':
        try:
            cursos = Matriculas.objects.filter(codigoAlumno = request.GET['codigoAlumno']).values('nombre')
            curso_serializer = CursosSerializer(cursos, many=True)
            print(curso_serializer)
            return JsonResponse(curso_serializer.data, safe=False)
        except Cursos.DoesNotExist:
            return JsonResponse("El usuario no cuenta con cursos registrados", safe=False)
        #resp_data = {'cantidadCursos': 1 }
