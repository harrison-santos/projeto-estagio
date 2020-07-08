from django import forms


from .models import Cliente, Endereco

class ClienteForm(forms.ModelForm):
    cpf = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    sobrenome = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    def __str__(self):
        return self.nome


    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'sobrenome', 'telefone', 'email']


class EnderecoForm(forms.ModelForm):
    logradouro = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    bairro = forms.CharField(
        widget=forms.TextInput()
    )
    cidade = forms.CharField(
        widget=forms.TextInput()
    )
    estado = forms.CharField(
        widget=forms.TextInput()
    )


    class Meta:
        model = Endereco
        fields = ['logradouro', 'bairro', 'cidade', 'estado']