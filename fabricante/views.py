from django.shortcuts import render, redirect
from fabricante.forms import FabricanteForm
from fabricante.models import Fabricante

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
