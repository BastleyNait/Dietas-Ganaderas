# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remov` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Alimento(models.Model):
    AliNom = models.CharField(db_column='AliNom', max_length=30)  # Field name made lowercase.
    AliCos = models.FloatField(db_column='AliCos', blank=True, null=True)  # Field name made lowercase.
    AliInfAña = models.TextField(db_column='AliInfAña', blank=True, null=True)  # Field name made lowercase.
    AliEstReg = models.CharField(db_column='AliEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    MagCod = models.ForeignKey('Magnitud', models.DO_NOTHING, db_column='MagCod', blank=True, null=True)  # Field name made lowercase.
    AliTipCod = models.ForeignKey('AlimentoTipo', models.DO_NOTHING, db_column='AliTipCod', blank=True, null=True)  # Field name made lowercase.
    AliCod = models.CharField(db_column='AliCod', primary_key=True, max_length=8)  # Field name made lowercase.

    def __str__(self):
        return self.AliNom;
    class Meta:
        db_table = 'alimento'



class AlimentoDietaToma(models.Model):
    DieCod = models.OneToOneField('Dieta', models.DO_NOTHING, db_column='DieCod', primary_key=True)  # Field name made lowercase. The composite primary key (DieCod, TomCod, AliCod) found, that is not supported. The first column is selected.
    TomCod = models.ForeignKey('Toma', models.DO_NOTHING, db_column='TomCod')  # Field name made lowercase.
    AliDieTomCan = models.DecimalField(db_column='AliDieTomCan', max_digits=4, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    AliDieTomEstReg = models.CharField(db_column='AliDieTomEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    AliCod = models.ForeignKey(Alimento, models.DO_NOTHING, db_column='AliCod')  # Field name made lowercase.

    class Meta:
        db_table = 'alimento dieta toma'
        unique_together = (('DieCod', 'TomCod', 'AliCod'),)


class AlimentoTipo(models.Model):
    AliTipCod = models.CharField(db_column='AliTipCod', primary_key=True, max_length=2)  # Field name made lowercase.
    AliTipDes = models.CharField(db_column='AliTipDes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    AliEstReg = models.CharField(db_column='AliEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'alimento tipo'


class Almacen(models.Model):
    AlmCod = models.CharField(db_column='AlmCod', primary_key=True, max_length=10)  # Field name made lowercase. The composite primary key (AlmCod, GraCod, EmpCod) found, that is not supported. The first column is selected.
    AlmNot = models.TextField(db_column='AlmNot', blank=True, null=True)  # Field name made lowercase.
    AlmEstReg = models.CharField(db_column='AlmEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    GraCod = models.ForeignKey('Granja', models.DO_NOTHING, db_column='GraCod',unique=True)  # Field name made lowercase.
    EmpCod = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='EmpCod', to_field='EmpCod', related_name='almacen_empcod_set',unique=True)  # Field name made lowercase.
    GraAlmCapMax = models.IntegerField(db_column='GraAlmCapMax')  # Field name made lowercase.      
    AlmCapMin = models.IntegerField(db_column='AlmCapMin')  # Field name made lowercase.

    def __str__(self):
        return self.AlmNot;

    class Meta:
        db_table = 'almacen'
        unique_together = (('AlmCod', 'GraCod', 'EmpCod'),)


class Animal(models.Model):
    AniCod = models.CharField(db_column='AniCod', primary_key=True, max_length=10)  # Field name made lowercase.
    AniPes = models.IntegerField(db_column='AniPes', blank=True, null=True)  # Field name made lowercase.
    AniAñoNac = models.IntegerField(db_column='AniAñoNac', blank=True, null=True)  # Field name made lowercase.
    AniPro = models.CharField(db_column='AniPro', max_length=10, blank=True, null=True)  # Field name made lowercase.
    AniDesDie = models.TextField(db_column='AniDesDie', blank=True, null=True)  # Field name made lowercase.
    AniEstReg = models.CharField(db_column='AniEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    AniUtiCod = models.ForeignKey('AnimalUtilidad', models.DO_NOTHING, db_column='AniUtiCod', blank=True, null=True)  # Field name made lowercase.
    AniTipCod = models.ForeignKey('AnimalTipo', models.DO_NOTHING, db_column='AniTipCod', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.AniCod;

    class Meta:
        db_table = 'animal'


class AnimalNutriente(models.Model):
    AniCod = models.OneToOneField(Animal, models.DO_NOTHING, db_column='AniCod', primary_key=True)  # Field name made lowercase. The composite primary key (AniCod, NutCod) found, that is not supported. The first column is selected.
    AniNutCanNes = models.IntegerField(db_column='AniNutCanNes', blank=True, null=True)  # Field name made lowercase.
    AniNutEstReg = models.CharField(db_column='AniNutEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    NutCod = models.ForeignKey('Nutriente', models.DO_NOTHING, db_column='NutCod')  # Field name made lowercase.

    class Meta:
        db_table = 'animal nutriente'
        unique_together = (('AniCod', 'NutCod'),)


class AnimalTipo(models.Model):
    AniTipCod = models.CharField(db_column='AniTipCod', primary_key=True, max_length=2)  # Field name made lowercase.
    AniUtiDes = models.CharField(db_column='AniUtiDes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    aniutieAniUtiEstRegstreg = models.CharField(db_column='AniUtiEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'animal tipo'


class AnimalUtilidad(models.Model):
    AniUtiCod = models.CharField(db_column='AniUtiCod', primary_key=True, max_length=1)  # Field name made lowercase.
    AniUtiDes = models.CharField(db_column='AniUtiDes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    AniUtiEstReg = models.CharField(db_column='AniUtiEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'animal utilidad'


class CabeceraPedido(models.Model):
    CabPedCod = models.IntegerField(db_column='CabPedCod', primary_key=True)  # Field name made lowercase.
    ProCod = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='ProCod')  # Field name made lowercase.
    CabPedEstReg = models.CharField(db_column='CabPedEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    AlmCod = models.ForeignKey('Almacen', models.DO_NOTHING, db_column='AlmCod')  # Field name made lowercase.
    GraCod = models.ForeignKey('Granja', models.DO_NOTHING, db_column='GraCod', to_field='GraCod', related_name='cabecerapedido_gracod_set')  # Field name made lowercase.
    EmpCod = models.ForeignKey('Empresa', models.DO_NOTHING, db_column='EmpCod', to_field='EmpCod', related_name='cabecerapedido_empcod_set')  # Field name made lowercase.
    def __str__(self):
        return str(self.CabPedCod);

    def get_granja(self):
        return self.GraCod.GraCod  # Suponiendo que Almacen tiene un campo relacionado llamado Granja

    def get_empresa(self):
        return self.EmpCod.EmpCod  # Suponiendo que Almacen tiene un campo relacionado llamado Empresa
    
    get_granja.short_description = 'Granja'
    get_empresa.short_description = 'Empresa'
    
    class Meta:
        db_table = 'cabecera pedido'





class DetallesDePedido(models.Model):
    DetPedHorLle = models.TimeField(db_column='DetPedHorLle', blank=True, null=True)  # Field name made lowercase.
    DetPedDiaLle = models.IntegerField(db_column='DetPedDiaLle', blank=True, null=True)  # Field name made lowercase.
    DetPedMesLle = models.IntegerField(db_column='DetPedMesLle', blank=True, null=True)  # Field name made lowercase.
    DetPedAñoLle = models.IntegerField(db_column='DetPedAñoLle', blank=True, null=True)  # Field name made lowercase.
    DetPedDes = models.TextField(db_column='DetPedDes', blank=True, null=True)  # Field name made lowercase.
    DetPedEstReg = models.CharField(db_column='DetPedEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    CabPedCod = models.OneToOneField(CabeceraPedido, models.DO_NOTHING, db_column='CabPedCod', primary_key=True)  # Field name made lowercase. The composite primary key (CabPedCod, AliCod) found, that is not supported. The first column is selected.
    AliCod = models.ForeignKey(Alimento, models.DO_NOTHING, db_column='AliCod')  # Field name made lowercase.


    def get_fecha(self):
        from datetime import date
        try:
            return date(self.DetPedAñoLle, self.DetPedMesLle, self.DetPedDiaLle)
        except ValueError:
            return None

    class Meta:
        db_table = 'detalles de pedido'
        unique_together = (('CabPedCod', 'AliCod'),)


class Dieta(models.Model):
    DieCod = models.CharField(db_column='DieCod', primary_key=True, max_length=10)  # Field name made lowercase.
    DieFin = models.CharField(db_column='DieFin', max_length=60, blank=True, null=True)  # Field name made lowercase.
    DieOtrDat = models.TextField(db_column='DieOtrDat', blank=True, null=True)  # Field name made lowercase.
    DieEstReg = models.CharField(db_column='DieEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.DieFin;
    class Meta:
        db_table = 'dieta'


class DietaAnimalFechaInicio(models.Model):
    DieAniFecDesRel = models.TextField(db_column='DieAniFecDesRel', blank=True, null=True)  # Field name made lowercase.
    DieAniFecEstReg = models.CharField(db_column='DieAniFecEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    AniCod = models.ForeignKey(Animal, models.DO_NOTHING, db_column='AniCod')  # Field name made lowercase.
    FecIniCod = models.OneToOneField('FechaInicio', models.DO_NOTHING, db_column='FecIniCod', primary_key=True)  # Field name made lowercase. The composite primary key (FecIniCod, DieCod, AniCod) found, that is not supported. The first column is selected.
    DieCod = models.ForeignKey(Dieta, models.DO_NOTHING, db_column='DieCod')  # Field name made lowercase.

    class Meta:
        db_table = 'dieta animal fecha inicio'
        unique_together = (('FecIniCod', 'DieCod', 'AniCod'),)


class Empresa(models.Model):
    EmpCod = models.IntegerField(db_column='EmpCod', primary_key=True)  # Field name made lowercase.
    EmpNom = models.CharField(db_column='EmpNom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    CiuCod = models.ForeignKey('Ciudad', models.DO_NOTHING, db_column='CiuCod', blank=True, null=True)  # Field name made lowercase.
    PaiCod = models.ForeignKey('Pais', models.DO_NOTHING, db_column='PaiCod', to_field='PaiCod', related_name='empresa_paicod_set')  # Field name made lowercase.
    def __str__ (self):
        return self.EmpNom;
    class Meta:
        db_table = 'empresa'


class Estado(models.Model):
    EstCod = models.CharField(db_column='EstCod', primary_key=True, max_length=1)  # Field name made lowercase.
    EstDes = models.CharField(db_column='EstDes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    EstEstReg = models.CharField(db_column='EstEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.EstDes;
    class Meta:
        db_table = 'estado'


class FechaInicio(models.Model):
    FecIniCod = models.IntegerField(db_column='FecIniCod', primary_key=True)  # Field name made lowercase.
    FecIniDia = models.IntegerField(db_column='FecIniDia', blank=True, null=True)  # Field name made lowercase.
    FecIniMes = models.IntegerField(db_column='FecIniMes', blank=True, null=True)  # Field name made lowercase.
    FecIniAño = models.IntegerField(db_column='FecIniAño', blank=True, null=True)  # Field name made lowercase.
    FecIniEstReg = models.CharField(db_column='FecIniEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.FecIniDia + '/' + self.FecIniMes + '/' + self.FecIniAño;
    class Meta:
        db_table = 'fecha inicio'


class Granja(models.Model):
    GraCod = models.CharField(db_column='GraCod', primary_key=True, max_length=10)  # Field name made lowercase. The composite primary key (GraCod, EmpCod) found, that is not supported. The first column is selected.
    GraNom = models.CharField(db_column='GraNom', max_length=60, blank=True, null=True)  # Field name made lowercase.
    GraNot = models.TextField(db_column='GraNot', blank=True, null=True)  # Field name made lowercase.
    GraEstReg = models.CharField(db_column='GraEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    CiuCod = models.ForeignKey('Ciudad', models.DO_NOTHING, db_column='CiuCod', blank=True, null=True)  # Field name made lowercase.
    EmpCod = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='EmpCod',unique=True)  # Field name made lowercase.
    PaiCod = models.ForeignKey('Pais', models.DO_NOTHING, db_column='PaiCod', to_field='PaiCod', related_name='granja_paicod_set', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.GraNom;

    class Meta:
        db_table = 'granja'
        unique_together = (('GraCod', 'EmpCod'),)


class Magnitud(models.Model):
    MagCod = models.CharField(db_column='MagCod', primary_key=True, max_length=2)  # Field name made lowercase.
    MagDes = models.CharField(db_column='MagDes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    MagEstReg = models.CharField(db_column='MagEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.MagDes;
    class Meta:
        db_table = 'magnitud'


class Nutriente(models.Model):
    NutNom = models.CharField(db_column='NutNom', max_length=10)  # Field name made lowercase.      
    NutInfRel = models.TextField(db_column='NutInfRel', blank=True, null=True)  # Field name made lowercase.
    NutEstReg = models.CharField(db_column='NutEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    EstCod = models.ForeignKey(Estado, models.DO_NOTHING, db_column='EstCod')  # Field name made lowercase.
    MagCod = models.ForeignKey(Magnitud, models.DO_NOTHING, db_column='MagCod', blank=True, null=True)  # Field name made lowercase.
    NutCod = models.CharField(db_column='NutCod', primary_key=True, max_length=9)  # Field name made lowercase.
    def __str__(self):
        return self.NutNom;
    class Meta:
        db_table = 'nutriente'


class NutrienteAlimento(models.Model):
    NutAliCanCon = models.IntegerField(db_column='NutAliCanCon', blank=True, null=True)  # Field name made lowercase.
    NutAliEstReg = models.CharField(db_column='NutAliEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    AliCod = models.OneToOneField(Alimento, models.DO_NOTHING, db_column='AliCod', primary_key=True)  # Field name made lowercase. The composite primary key (AliCod, NutCod) found, that is not supported. The first column is selected.
    NutCod = models.ForeignKey(Nutriente, models.DO_NOTHING, db_column='NutCod')  # Field name made lowercase.

    class Meta:
        db_table = 'nutriente alimento'
        unique_together = (('AliCod', 'NutCod'),)


class Pais(models.Model):
    PaiCod = models.IntegerField(db_column='PaiCod', primary_key=True)  # Field name made lowercase.
    PaiDes = models.CharField(db_column='PaiDes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    PaiEstReg = models.CharField(db_column='PaiEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.PaiDes;
    class Meta:
        db_table = 'pais'

class Ciudad(models.Model):
    CiuCod = models.CharField(db_column='CiuCod', primary_key=True, max_length=2)  # Field name made lowercase. The composite primary key (CiuCod, PaiCod) found, that is not supported. The first column is selected.
    CiuDes = models.CharField(db_column='CiuDes', max_length=20, blank=True, null=True)  # Field name made lowercase.
    CiuEstReg = models.CharField(db_column='CiuEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    PaiCod = models.ForeignKey('Pais', models.DO_NOTHING, db_column='PaiCod')  # Field name made lowercase.

    def __str__(self):
        return self.CiuDes;

    class Meta:
        db_table = 'ciudad'
        constraints = [
            models.UniqueConstraint(fields=['CiuCod', 'PaiCod'], name='unique_ciudad_pais')
        ]

class Proveedores(models.Model):
    ProCod = models.CharField(db_column='ProCod', primary_key=True, max_length=10)  # Field name made lowercase.
    ProNom = models.CharField(db_column='ProNom', max_length=30, blank=True, null=True)  # Field name made lowercase.
    ProCon = models.CharField(db_column='ProCon', max_length=9, blank=True, null=True)  # Field name made lowercase.
    ProInfFis = models.CharField(db_column='ProInfFis', unique=True, max_length=8)  # Field name made lowercase.
    ProDes = models.TextField(db_column='ProDes', blank=True, null=True)  # Field name made lowercase.
    ProEstReg = models.CharField(db_column='ProEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    CiuCod = models.ForeignKey('Ciudad', models.DO_NOTHING, db_column='CiuCod', blank=True, null=True)  # Field name made lowercase.
    PaiCod = models.ForeignKey('Pais', models.DO_NOTHING, db_column='PaiCod', to_field='PaiCod', related_name='proveedores_paicod_set', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.ProNom;
    class Meta:
        db_table = 'proveedores'


class Stock(models.Model):
    AlmCod = models.OneToOneField(Almacen, models.DO_NOTHING, db_column='AlmCod', primary_key=True)  # Field name made lowercase. The composite primary key (AlmCod, GraCod, EmpCod, AliCod) found, that is not supported. The first column is selected.
    StoEst = models.CharField(db_column='StoEst', max_length=1, blank=True, null=True)  # Field name made lowercase.
    StoCanDis = models.IntegerField(db_column='StoCanDis', blank=True, null=True)  # Field name made lowercase.
    StoEstReg = models.CharField(db_column='StoEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    GraCod = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='GraCod', to_field='GraCod', related_name='stock_gracod_set')  # Field name made lowercase.
    EmpCod = models.ForeignKey(Almacen, models.DO_NOTHING, db_column='EmpCod', to_field='EmpCod', related_name='stock_empcod_set')  # Field name made lowercase.
    AliCod = models.ForeignKey(Alimento, models.DO_NOTHING, db_column='AliCod')  # Field name made lowercase.
    def __str__(self):
        return str(self.StoEs);
    class Meta:
        db_table = 'stock'
        unique_together = (('AlmCod', 'GraCod', 'EmpCod', 'AliCod'),)


class Toma(models.Model):
    TomCod = models.IntegerField(db_column='TomCod', primary_key=True)  # Field name made lowercase.
    TomNom = models.CharField(db_column='TomNom', max_length=20, blank=True, null=True)  # Field name made lowercase.
    TomHorIni = models.TimeField(db_column='TomHorIni', blank=True, null=True)  # Field name made lowercase.
    TomHorFin = models.TimeField(db_column='TomHorFin', blank=True, null=True)  # Field name made lowercase.
    TomOtrDat = models.TextField(db_column='TomOtrDat', blank=True, null=True)  # Field name made lowercase.
    TomEstReg = models.CharField(db_column='TomEstReg', max_length=1, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.TomNom;
    class Meta:
        db_table = 'toma'