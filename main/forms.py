from django import forms

class RegistrarUsuarioForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Seu nome completo'}),
        max_length=80
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Seu melhor email'})
    )
    cpf = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Seu cpf'}),
        max_length=11
    )
    senha = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Insira uma boa senha'}),
        max_length=11
    )

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Seu email'})
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Sua senha'}),
        max_length=20
    )