from django import forms

class FabricanteForm(forms.Form):
    codigo = forms.IntegerField(label='Código')
    nome = forms.CharField(label='Nome', max_length=70)