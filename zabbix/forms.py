from django import forms
from banco.models import HostsAtivosZB

class HostsAtivosZBModelForm(forms.ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     for field_name in self.fields:
    #         self.fields[field_name].required = False    

    class Meta:
        model = HostsAtivosZB
        fields = '__all__'
        exclude = ['id']




# class MeuFormulario(forms.Form):
#     meu_campo = forms.CharField(
#         required=False,
#         error_messages={
#             'required': 'Esta mensagem não será exibida porque o campo não é obrigatório.'
#         }
#     )