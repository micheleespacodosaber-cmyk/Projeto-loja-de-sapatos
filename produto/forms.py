from django import forms

class ProdutoForm(forms.Form):
    codigo = forms.IntegerField(label='Código')
    nome = forms.CharField(max_length=70, label='Nome')
    preco_compra = forms.FloatField(label='Preço de compra')
    preco_venda = forms.FloatField(label='Preço de venda')
    cor = forms.CharField(max_length=20, label='Cor')
    data_fabricacao = forms.DateField(label='Data de fabricação',input_formats=['%d/%m/%Y'],widget=forms.DateInput(attrs={'placeholder': 'dd/mm/aaaa'}))
    imagem = forms.CharField(max_length=25, label='Imagem')
