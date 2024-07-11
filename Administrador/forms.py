from django import forms
from .models import Pais, Ciudad, Empresa


class GranjaForm(forms.Form):
    GraCod = forms.IntegerField(
    widget=forms.NumberInput(attrs={'class': 'form-control-sm'})
    )
    GraNom = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    GraNot = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3})
    )
    GraEstReg = forms.ChoiceField(
        choices=[('A', 'Activo'), ('I', 'Inactivo'), ('*', 'Eliminado')],
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    CiuCod = forms.ModelChoiceField(
        queryset=Ciudad.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    EmpCod = forms.ModelChoiceField(
        queryset=Empresa.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    PaiCod = forms.ModelChoiceField(
        queryset=Pais.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select'})
    )