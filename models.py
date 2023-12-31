# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BancoAutor(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'banco_autor'


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


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
