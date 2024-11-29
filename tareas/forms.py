from django import forms
from .models import Tarea
#datos que el usario va a manejar
class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields =['titulo', 'descripcion', 'completada']