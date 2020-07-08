from django.shortcuts import render, redirect
from .models import Cliente, Endereco
from .forms import ClienteForm, EnderecoForm

# Create your views here.

def clientesListar(request):
    clientes = Cliente.objects.all()
    args = {'clientes': clientes}

    return render(request, 'clientes/clientes_listar.html', args)


def clientesCadastrar(request):
    form = ClienteForm(request.POST)
    args = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('clientesListar')
    return render(request, 'clientes/clientes_cadastrar.html', args)

def clientesDeletar(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)

    if cliente:
        cliente.delete()
    return redirect('clientesListar')

def clientesEditar(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    form = ClienteForm(request.POST or None, instance=cliente)
    args = {'form': form}

    if form.is_valid():
        form.save()
        return redirect('clientesListar')

    return render(request, 'clientes/clientes_editar.html', args)




def enderecosListar(request, cliente_id):
    enderecos = Endereco.objects.all().filter(cliente=cliente_id)
    args = {'enderecos': enderecos, 'cliente_id': cliente_id}

    return render(request, "clientes/enderecos_listar.html", args)

def enderecosCadastrar(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    form = EnderecoForm(request.POST)
    args = {'form': form}

    if request.method == 'POST':
        endereco = form.save(commit=False)
        endereco.cliente = cliente

        if form.is_valid():
            form.save()
            return redirect('enderecosListar', cliente_id=cliente_id)

    return render(request, 'clientes/enderecos_cadastrar.html', args)

def enderecosDeletar(request, cliente_id, endereco_id):
    endereco = Endereco.objects.get(pk=endereco_id)

    if endereco:
        endereco.delete()
    return redirect('enderecosListar', cliente_id=cliente_id)


def enderecosEditar(request, cliente_id, endereco_id):
    endereco = Endereco.objects.get(pk=endereco_id)
    cliente = Cliente.objects.get(pk=cliente_id)
    form = EnderecoForm(request.POST or None, instance=endereco)
    args = {'form': form}

    if request.method == 'POST':
        endereco = form.save(commit=False)
        endereco.cliente = cliente

        if form.is_valid():
            form.save()
            return redirect('enderecosListar', cliente_id=cliente_id)

    return render(request, 'clientes/enderecos_editar.html', args)
