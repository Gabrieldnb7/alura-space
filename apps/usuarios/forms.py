from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Usuário',
        required=True,
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Digite seu usuário'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Digite sua senha'

            }
        )
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label="Nome completo",
        required=True,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                "placeholder": 'Nome completo'
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=50,
        widget=forms.EmailInput(
            attrs= {
                "class": 'form-control',
                "placeholder": 'Digite seu email'
            }
        )
    )
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs= {
                "class": 'form-control',
                "placeholder": 'Digite sua senha'
            }
        )
    )
    senha_2 = forms.CharField(
        label='Confirmar Senha',
        required=True,
        max_length=20,
        widget=forms.PasswordInput(
            attrs= {
                "class": 'form-control',
                "placeholder": 'Confirme sua senha'
            }
        )
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')
        if nome:
            nome = nome.strip()
            if " " in nome:
                raise forms.ValidationError("Não é permitido espaços nesse campo.")
            else:
                return nome
    
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais.')
            else:
                return senha_2