from django import forms
from banco.models import HostsAtivosZB, Empresa, Pais, Localidade,TipoLocal



class HostsAtivosZBAdminForm(forms.ModelForm):
    class Meta:
        model = HostsAtivosZB
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pais'].queryset = Pais.objects.none()
        self.fields['tipo_localidade'].queryset = TipoLocal.objects.none()
        self.fields['localidade'].queryset = Localidade.objects.none()
        self.fields['empresa'].queryset = Empresa.objects.none()

    