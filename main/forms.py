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
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Sua senha'}),
        max_length=20
    )

class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'input-field', 'placeholder': 'Seu email'})
    )
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-field', 'placeholder': 'Sua senha'}),
        max_length=20
    )

class RegistrarInsumoForm(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Insira o nome da Insumo'}),
        max_length=100
        )
    descricao = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Descrição do insumo'})
    )
    unidade_medida = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'input-field', 'placeholder': 'Unidade de medida[L/Kg]'}),
        max_length=50
    )
