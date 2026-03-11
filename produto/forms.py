from django import forms

class ProdutoForm(forms.Form):
    codigo = forms.IntegerField()
    nome = forms.CharField(max_length=70)
    preco_compra = forms.FloatField()
    preco_venda = forms.FloatField()
    cor = forms.CharField(max_length=20)
    data_fabricacao = forms.DateField()
    imagem = forms.CharField(max_length=25)
    