from django.shortcuts import render, get_object_or_404, redirect
from Producao.models import Coleta, Criacao
from Producao.forms import ColetaForm, CriacaoForm

def home(request):
    return render(request, 'Producao/index.html')

def listar_coletas(request):
    coletas = Coleta.objects.all().order_by('-data')
    return render(request, 'Producao/listar_coletas.html', {'lista_coletas': coletas})

def detalhes_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, id=coleta_id)
    return render(request, 'Producao/detalhes_coleta.html', {'coleta': coleta})

def deletar_coleta(request, coleta_id):
    coleta = get_object_or_404(Coleta, id=coleta_id)
    if request.method == 'POST':
        coleta.delete()
        return redirect('listar_coletas')
    return render(request, 'Producao/confirmar_delecao.html', {'coleta': coleta})

def criar_coleta(request):
    if request.method == 'POST':
        form = ColetaForm(request.POST)
        if form.is_valid():
            criacao = form.cleaned_data['criacao']
            data = form.cleaned_data['data']
            quantidade = form.cleaned_data['quantidade']
            Coleta.objects.create(
                criacao=criacao,
                data=data,
                quantidade=quantidade
            )

            informacoes = {
                'lista_coletas': Coleta.objects.all()
            }

            return render(request, 'Producao/listar_coletas.html', informacoes)
    form = ColetaForm()
    return render(request, 'Producao/criar_coleta.html', {'form': form})

def criar_criacao(request):
    if request.method == 'POST':
        form = CriacaoForm(request.POST)
        if form.is_valid():
            raca = form.cleaned_data['raca']
            data_entrada = form.cleaned_data['data_entrada']

            Criacao.objects.create(raca=raca, data_entrada=data_entrada)

            informacoes = {
                'lista_criacoes': Criacao.objects.all()
            }

            return render(request, 'Producao/listar_criacoes.html', informacoes)
    else:
        form = CriacaoForm()
    return render(request, 'Producao/criar_criacao.html', {'form': form})

def listar_criacoes(request):
    lista_criacoes = Criacao.objects.all()

    return render(request, 'Producao/listar_criacoes.html', {'lista_criacoes': lista_criacoes})