from django import forms
from .models import PerfilUsuario, Usuario

class PerfilUsuarioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['biografia', 'foto_perfil']
        
class RegistroUsuarioForm(forms.ModelForm):
    contrasena = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombres', 'nombre_usuario', 'email', 'contrasena']