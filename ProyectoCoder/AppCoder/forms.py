# AppCoder/forms.py
from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    comision = forms.CharField(max_length=100)
