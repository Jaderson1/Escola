from django.contrib import admin
from django.urls import include, path
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculaCurso, ListaMatriculaEstudante
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'estudantes', EstudanteViewSet, basename='estudantes')
router.register(r'cursos', CursoViewSet, basename='cursos')
router.register('matriculas',MatriculaViewSet,basename='Matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculaEstudante.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaMatriculaCurso.as_view()),
]