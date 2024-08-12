from django import forms


class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(max_length=80)
    email = forms.EmailField()
    cpf = forms.CharField(max_length=11)

class loginForm(forms.Form):
    email = forms.EmailField()
    senha = forms.CharField(max_length=20)
