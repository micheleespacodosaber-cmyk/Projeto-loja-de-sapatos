from django import forms

class FabricanteForm(forms.Form):
    codigo = forms.IntegerField(required=True)
    nome = forms.CharField(max_length=70, required=True)

class ContatoSacForm(forms.Form):
    nome_completo = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    telefone = forms.CharField(max_length=11, required=True)
    melhor_hora_contato = forms.ChoiceField(
        choices=[
            ('', 'Selecione'),
            ('Manhã', 'Manhã'),
            ('Tarde', 'Tarde'),
            ('Noite', 'Noite'),
        ],
        required=True
    )
    mensagem = forms.CharField(max_length=1024, required=True)