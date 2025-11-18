# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Receita

# (US 2) Lógica para LISTAR
def listar_receitas(request):
    receitas = Receita.objects.all().order_by('-id') # Mais novas primeiro
    return render(request, 'core/listar.html', {'receitas': receitas})

# (US 3) Lógica para DETALHAR
def detalhe_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    return render(request, 'core/detalhe.html', {'receita': receita})

# (US 1) Lógica para CADASTRAR
def cadastrar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_receitas')
    else:
        form = ReceitaForm()

    # Renderiza o formulário (com erros quando existir)
    return render(request, 'core/form_receita.html', {'form': form})

# (US 4) Lógica para EXCLUIR
def excluir_receita(request, pk):
    receita = get_object_or_404(Receita, pk=pk)
    
    if request.method == 'POST':
        # Se o formulário de confirmação foi enviado
        receita.delete()
        return redirect('listar_receitas')
    
    # Se for acesso GET, mostra a página de confirmação
    return render(request, 'core/confirmar_exclusao.html', {'receita': receita})