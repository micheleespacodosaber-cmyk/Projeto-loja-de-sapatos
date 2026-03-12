from django.shortcuts import render, redirect
from fabricante.forms import FabricanteForm, ContatoSacForm
from fabricante.models import Fabricante, ContatoSac

def cadastro(request):
    if request.method == 'POST':
        form = FabricanteForm(request.POST)

        if form.is_valid():
            fabricante = Fabricante(
                codigo=form.cleaned_data['codigo'],
                nome=form.cleaned_data['nome']
            )
            fabricante.save()
            return redirect('fabricante:cadastro')
    else:
        form = FabricanteForm()

    return render(request, 'fabricante/cadastro.html', {'form': form})

def listar(request):
    lista_fabricantes = Fabricante.objects.all()
    return render(request, 'fabricante/lista.html', {'fabricantes': lista_fabricantes})

def excluir(request, codigoFabricante):
    fabricante = Fabricante.objects.get(pk=codigoFabricante)
    fabricante.delete()
    return redirect('fabricante:listar')

def contato(request):
    mensagem_sucesso = False

    if request.method == 'POST':
        form = ContatoSacForm(request.POST)

        if form.is_valid():
            contato = ContatoSac(
                nome_completo=form.cleaned_data['nome_completo'],
                email=form.cleaned_data['email'],
                telefone=form.cleaned_data['telefone'],
                melhor_hora_contato=form.cleaned_data['melhor_hora_contato'],
                mensagem=form.cleaned_data['mensagem']
            )
            contato.save()
            form = ContatoSacForm()
            mensagem_sucesso = True
    else:
        form = ContatoSacForm()

    return render(
        request,
        'contato.html',
        {
            'form': form,
            'mensagem_sucesso': mensagem_sucesso
        }
    )