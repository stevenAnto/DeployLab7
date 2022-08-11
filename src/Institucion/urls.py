from django.urls import re_path
from Institucion import views
from Institucion.routers import router

urlpatterns = [
    re_path(r'^misCursos$', views.misCursosApi, name="misCursos"),
    re_path(r'^loginAdmin$', views.loginAdminApi, name="loginAdmin"),
    re_path(r'^detail$', views.detailApi, name="detail"),
    # re_path(r'^profesores$', views.profesorApi, name="profesor"),
    # re_path(r'^profesores/([0-9]+)$', views.profesorApi),
    # re_path(r'^cursos$', views.cursosApi, name="curso"),
    # re_path(r'^cursos/([0-9]+)$', views.cursosApi),
    # re_path(r'^alumnos$', views.alumnoApi, name="alumno"),
    # re_path(r'^alumnos/([0-9]+)$', views.alumnoApi),
    # re_path(r'^admin$', views.adminApi, name="admin"),
    # re_path(r'^admin/([0-9]+)$', views.adminApi)
]

urlpatterns += router.urls