from django import forms

class ProdutoForm(forms.Form):
    codigo = forms.IntegerField(required=True)
    nome = forms.CharField(max_length=70, required=True)
    preco_compra = forms.FloatField(required=True)
    preco_venda = forms.FloatField(required=True)
    cor = forms.CharField(max_length=20, required=True)
    data_fabricacao = forms.DateField(
        input_formats=['%d/%m/%Y'],
        required=True
    )
    imagem = forms.CharField(max_length=25, required=True)
