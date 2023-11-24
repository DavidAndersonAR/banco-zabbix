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


class HostsAtivos(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    host = models.CharField(db_column='Host', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    acn = models.CharField(db_column='ACN', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    ambiente = models.CharField(db_column='Ambiente', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    critico = models.CharField(db_column='Critico', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    local = models.CharField(db_column='Local', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    ons = models.CharField(db_column='ONS', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    pais = models.CharField(db_column='Pais', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    sublocal = models.CharField(db_column='SubLocal', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    subtipo = models.CharField(db_column='SubTipo', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    tipo = models.CharField(db_column='Tipo', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    ambiente_relatorio = models.CharField(db_column='Ambiente_Relatorio', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    comunicacao = models.CharField(db_column='Comunicacao', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    escopo = models.CharField(db_column='Escopo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    familia = models.CharField(db_column='Familia', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    filtros = models.CharField(db_column='Filtros', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    horario_relatorio = models.CharField(db_column='Horario_Relatorio', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    localidade = models.CharField(db_column='Localidade', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    operadora = models.CharField(db_column='Operadora', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    relatorio = models.CharField(db_column='Relatorio', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    servico = models.CharField(db_column='Servico', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    tagrelatorio = models.CharField(db_column='TagRelatorio', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    tipo02 = models.CharField(db_column='Tipo02', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.
    empresa = models.CharField(db_column='Empresa', max_length=255, db_collation='latin1_swedish_ci', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hosts_ativos'
