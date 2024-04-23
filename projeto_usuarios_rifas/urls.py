from django.urls import path
from app_cadastro import views

urlpatterns = [
    path('', views.home, name="home"),
    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    path('usuarios/excluir/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),  # Nova rota para exclusão de usuário
]
