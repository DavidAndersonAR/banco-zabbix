from django.contrib import admin
from .models import DisponibilidadeHosts, BancoAutor, BancoMotivos, HostsAtivosZB, TipoLocal, Pais, Empresa, Localidade

class DisponibilidadeHostsAdmin(admin.ModelAdmin):
    list_display = ('id_banco', 'id', 'host', 'data_coleta', 'disponibilidade', 'disp_expurgada', 'status')
    list_filter = ('status', 'data_coleta')
    search_fields = ['host', 'status']  # Adicione os campos pelos quais você quer permitir a busca

admin.site.register(DisponibilidadeHosts, DisponibilidadeHostsAdmin)

class HostsAtivosZBAdmin(admin.ModelAdmin):
    list_display = ('id', 'host', 'localidade', 'local', 'status', 'horario_relatorio', 'comunicacao')
    list_filter = ('status', 'localidade')
    search_fields = ['host', 'status', 'localidade']


admin.site.register(HostsAtivosZB, HostsAtivosZBAdmin)
admin.site.register(BancoAutor)
admin.site.register(BancoMotivos)
admin.site.register(TipoLocal)
admin.site.register(Pais)
admin.site.register(Empresa)
admin.site.register(Localidade)

