from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request, "usuarios/home.html") 

def usuarios(request):
    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.telefone = request.POST.get('telefone')
        novo_usuario.numeroRifa = request.POST.get('numeroRifa')
        novo_usuario.pago = request.POST.get('pago')

        if not Usuario.objects.filter(nome=novo_usuario.nome, telefone=novo_usuario.telefone, numeroRifa=novo_usuario.numeroRifa).exists():
            novo_usuario.save()
            return redirect("listagem_usuarios")  

    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    return render(request, "usuarios/usuarios.html", usuarios)

def excluir_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    usuario.delete()
    return redirect("listagem_usuarios")
