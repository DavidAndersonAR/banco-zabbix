from django.db import models

# Create your models here.



class BancoAutor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'banco_autor'

    def __str__(self):
        return self.nome


class BancoMotivos(models.Model):
    id = models.BigAutoField(primary_key=True)
    descricao = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'banco_motivos'


class DisponibilidadeHosts(models.Model):
    id = models.IntegerField()
    host = models.CharField(max_length=100)
    data_coleta = models.DateField()
    disponibilidade = models.CharField(max_length=45, blank=True, null=True)
    disp_expurgada = models.CharField(max_length=45, blank=True, null=True)
    status = models.CharField(max_length=45, blank=True, null=True)
    id_banco = models.AutoField(primary_key=True)
    autor = models.ForeignKey(BancoAutor, models.DO_NOTHING, blank=True, null=True)
    motivos = models.ForeignKey(BancoMotivos, models.DO_NOTHING, blank=True, null=True)
    percentual_expurgo = models.CharField(max_length=45, blank=True, null=True)
    comentarios = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disponibilidade_hosts'



class Localidade(models.Model):
    id = models.IntegerField(primary_key=True)
    localidade = models.CharField(max_length=50)

    def __str__(self):
        return self.localidade

class TipoLocal(models.Model):
    tipo_local = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_local
    
class Pais(models.Model):
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.pais

class Empresa(models.Model):
    empresa = models.CharField(max_length=50)

    def __str__(self):
        return self.empresa




class HostsAtivosZB(models.Model):
    id = models.IntegerField(primary_key=True)
    host = models.CharField(max_length=100)
    ip = models.CharField(max_length=50)  
    acn = models.CharField(max_length=50)  
    ambiente = models.CharField(max_length=50)  
    critico = models.CharField(max_length=50)  
    local = models.CharField(max_length=50)  
    ons = models.CharField(max_length=50)  
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_localidade = models.ForeignKey(TipoLocal, on_delete=models.SET_NULL, null=True)
    subtipo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)  
    ambiente_relatorio = models.CharField(max_length=50)
    comunicacao = models.CharField(max_length=50)
    escopo = models.CharField(max_length=50)  
    familia = models.CharField(max_length=50)  
    filtros = models.CharField(max_length=50)  
    horario_relatorio = models.CharField(max_length=50)  
    localidade = models.ForeignKey(Localidade, on_delete=models.SET_NULL, null=True, blank=True)
    operadora = models.CharField(max_length=50)
    relatorio = models.CharField(max_length=50)
    servico = models.CharField(max_length=50)  
    status = models.CharField(max_length=50)  
    tagrelatorio = models.CharField(max_length=50)
    tipo02 = models.CharField(max_length=50)  
    empresa = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True, blank=True)

