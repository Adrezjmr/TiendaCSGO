from django import forms

class nuevoContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", max_length=200)
    descripcion = forms.CharField(label="Descripcion",widget=forms.Textarea)
    widgets = {
        'nombre' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : "Escribe tu nombre"}),
        'descripcion' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : "Escribenos tu mensaje"})
    }
