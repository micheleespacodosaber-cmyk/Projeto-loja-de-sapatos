from django.shortcuts import render, redirect
from produto.forms import ProdutoForm
from produto.models import Produto

def cadastro(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

        if form.is_valid():
            produto = Produto(
                codigo=form.cleaned_data['codigo'],
                nome=form.cleaned_data['nome'],
                preco_compra=form.cleaned_data['preco_compra'],
                preco_venda=form.cleaned_data['preco_venda'],
                cor=form.cleaned_data['cor'],
                data_fabricacao=form.cleaned_data['data_fabricacao'],
                imagem=form.cleaned_data['imagem']
            )
            produto.save()
            return redirect('produto:cadastro')
    else:
        form = ProdutoForm()

    return render(request, 'produto/cadastro.html', {'form': form})

def listar(request):
    lista_produtos = Produto.objects.all()
    return render(request, 'produto/lista.html', {'produtos': lista_produtos})
def excluir(request, codigoProduto):
    produto = Produto.objects.get(pk=codigoProduto)
    produto.delete()
    return redirect('produto:listar')