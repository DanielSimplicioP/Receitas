from django import forms
from .models import Receita


class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = ['nome', 'ingredientes', 'modo_preparo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Bolo de Chocolate Cremoso'}),
            'ingredientes': forms.Textarea(attrs={'class': 'form-control', 'rows': 8, 'placeholder': 'Ex: 2 xícaras de farinha, 1 xícara de açúcar...'}),
            'modo_preparo': forms.Textarea(attrs={'class': 'form-control', 'rows': 12, 'placeholder': 'Ex: 1. Misture os ingredientes secos... 2. Adicione os líquidos...'}),
        }
