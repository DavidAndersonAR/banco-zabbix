from django.contrib import admin
from .models import DisponibilidadeHosts, BancoAutor, BancoMotivos

class DisponibilidadeHostsAdmin(admin.ModelAdmin):
    list_display = ('id_banco', 'id', 'host', 'data_coleta', 'disponibilidade', 'disp_expurgada', 'status')
    list_filter = ('status', 'data_coleta')
    search_fields = ['host', 'status']  # Adicione os campos pelos quais você quer permitir a busca

admin.site.register(DisponibilidadeHosts, DisponibilidadeHostsAdmin)

admin.site.register(BancoAutor)
admin.site.register(BancoMotivos)
