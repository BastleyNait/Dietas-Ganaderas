# admin.py

from django.contrib import admin
from .models import (
    Animal, Nutriente, Alimento, Toma, Dieta, Granja, Proveedores, Almacen,
    FechaInicio, AnimalNutriente, DietaAnimalFechaInicio, NutrienteAlimento,
    AlimentoDietaToma, Stock, Ciudad, Magnitud, Estado, AnimalTipo, AnimalUtilidad,
    AlimentoTipo, CabeceraPedido, Empresa, Pais, 
    DetallesDePedido
)

class AnimalAdmin(admin.ModelAdmin):
    list_display = ('AniCod', 'AniPes', 'AniAñoNac', 'AniPro', 'AniDesDie', 'AniEstReg', 'AniUtiCod', 'AniTipCod')
    search_fields = ('AniCod', 'AniPro', 'AniDesDie', 'AniUtiCod', 'AniTipCod')
    list_editable = ('AniDesDie', 'AniEstReg')

class NutrienteAdmin(admin.ModelAdmin):
    list_display = ('NutCod', 'NutNom', 'NutInfRel', 'NutEstReg', 'EstCod', 'MagCod')
    search_fields = ('NutCod', 'NutNom', 'NutInfRel', 'EstCod', 'MagCod')
    list_editable = ('NutNom', 'NutEstReg')

class AlimentoAdmin(admin.ModelAdmin):
    list_display = ('AliCod', 'AliNom', 'AliCos', 'AliInfAña', 'AliEstReg', 'MagCod', 'AliTipCod')
    search_fields = ('AliCod', 'AliNom', 'AliInfAña', 'MagCod', 'AliTipCod')
    list_editable = ('AliNom', 'AliEstReg')

class TomaAdmin(admin.ModelAdmin):
    list_display = ('TomCod', 'TomNom', 'TomHorIni', 'TomHorFin', 'TomOtrDat', 'TomEstReg')
    search_fields = ('TomCod', 'TomNom', 'TomOtrDat')
    list_editable = ('TomNom', 'TomEstReg')

class DietaAdmin(admin.ModelAdmin):
    list_display = ('DieCod', 'DieFin', 'DieOtrDat', 'DieEstReg')
    search_fields = ('DieCod', 'DieFin', 'DieOtrDat')
    list_editable = ('DieOtrDat', 'DieEstReg')

class GranjaAdmin(admin.ModelAdmin):
    list_display = ('GraCod', 'GraNom', 'GraNot', 'GraEstReg', 'CiuCod', 'EmpCod', 'PaiCod')
    search_fields = ('GraCod', 'GraNom', 'GraNot', 'CiuCod', 'EmpCod', 'PaiCod')
    list_editable = ('GraNom', 'GraEstReg')

class ProveedoresAdmin(admin.ModelAdmin):
    list_display = ('ProCod', 'ProNom', 'ProCon', 'ProInfFis', 'ProDes', 'ProEstReg', 'CiuCod', 'PaiCod')
    search_fields = ('ProCod', 'ProNom', 'ProCon', 'ProInfFis', 'ProDes', 'CiuCod', 'PaiCod')
    list_editable = ('ProNom', 'ProEstReg')

class AlmacenAdmin(admin.ModelAdmin):
    list_display = ('AlmCod', 'AlmNot', 'AlmEstReg', 'GraCod', 'EmpCod', 'AlmCapMin', 'GraAlmCapMax')
    search_fields = ('AlmCod', 'AlmNot', 'GraCod', 'EmpCod')
    list_editable = ('AlmNot', 'AlmEstReg')

class FechaInicioAdmin(admin.ModelAdmin):
    list_display = ('FecIniCod', 'FecIniDia', 'FecIniMes', 'FecIniAño', 'FecIniEstReg')
    search_fields = ('FecIniCod', 'FecIniDia', 'FecIniMes', 'FecIniAño')
    list_editable = ('FecIniDia', 'FecIniEstReg')

class AnimalNutrienteAdmin(admin.ModelAdmin):
    list_display = ('AniCod', 'NutCod', 'AniNutCanNes', 'AniNutEstReg')
    search_fields = ('AniCod', 'NutCod')
    list_editable = ('AniNutCanNes', 'AniNutEstReg')

class DietaAnimalFechaInicioAdmin(admin.ModelAdmin):
    pass
class NutrienteAlimentoAdmin(admin.ModelAdmin):
    list_display = ('NutCod', 'AliCod', 'NutAliCanCon', 'NutAliEstReg')
    search_fields = ('NutCod', 'AliCod')
    list_editable = ('NutAliCanCon', 'NutAliEstReg')

class AlimentoDietaTomaAdmin(admin.ModelAdmin):
    list_display = ('DieCod', 'TomCod', 'AliCod', 'AliDieTomCan', 'AliDieTomEstReg')
    search_fields = ('DieCod', 'TomCod', 'AliCod')
    list_editable = ('AliDieTomCan', 'AliDieTomEstReg')

class StockAdmin(admin.ModelAdmin):
    list_display = ('AlmCod', 'GraCod', 'EmpCod', 'AliCod', 'StoEst', 'StoCanDis', 'StoEstReg')
    search_fields = ('AlmCod', 'GraCod', 'EmpCod', 'AliCod')
    list_editable = ('StoCanDis', 'StoEstReg')

class CiudadAdmin(admin.ModelAdmin):
    list_display = ('CiuCod', 'CiuDes', 'CiuEstReg', 'PaiCod')
    search_fields = ('CiuCod', 'CiuDes', 'PaiCod')
    list_editable = ('CiuDes', 'CiuEstReg')

class MagnitudAdmin(admin.ModelAdmin):
    list_display = ('MagCod', 'MagDes', 'MagEstReg')
    search_fields = ('MagCod', 'MagDes')
    list_editable = ('MagDes', 'MagEstReg')

class EstadoAdmin(admin.ModelAdmin):
    list_display = ('EstCod', 'EstDes', 'EstEstReg')
    search_fields = ('EstCod', 'EstDes')
    list_editable = ('EstDes', 'EstEstReg')

class AnimalTipoAdmin(admin.ModelAdmin):
    list_display = ('AniTipCod', 'AniUtiDes')
    search_fields = ('AniTipCod', 'AniUtiDes')

class AnimalUtilidadAdmin(admin.ModelAdmin):
    list_display = ('AniUtiCod', 'AniUtiDes', 'AniUtiEstReg')
    search_fields = ('AniUtiCod', 'AniUtiDes')
    list_editable = ('AniUtiDes', 'AniUtiEstReg')

class AlimentoTipoAdmin(admin.ModelAdmin):
    list_display = ('AliTipCod', 'AliTipDes', 'AliEstReg')
    search_fields = ('AliTipCod', 'AliTipDes')
    list_editable = ('AliTipDes', 'AliEstReg')

class CabeceraPedidoAdmin(admin.ModelAdmin):
    list_display = ('CabPedCod', 'ProCod', 'CabPedEstReg', 'AlmCod', 'get_granja', 'get_empresa')
    search_fields = ('CabPedCod', 'ProCod', 'AlmCod', 'GraCod', 'EmpCod')
    list_editable = ('CabPedEstReg',)

class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('EmpCod', 'EmpNom', 'CiuCod', 'PaiCod')
    search_fields = ('EmpCod', 'EmpNom', 'CiuCod', 'PaiCod')
    list_editable = ('EmpNom', )

class PaisAdmin(admin.ModelAdmin):
    list_display = ('PaiCod', 'PaiDes', 'PaiEstReg')
    search_fields = ('PaiCod', 'PaiDes')
    list_editable = ('PaiDes', 'PaiEstReg')

class DetallesDePedidoAdmin(admin.ModelAdmin):
    list_display = ('CabPedCod', 'AliCod', 'DetPedHorLle', 'DetPedDiaLle', 'DetPedMesLle', 'DetPedAñoLle', 'DetPedDes', 'DetPedEstReg')
    search_fields = ('CabPedCod', 'AliCod')
    list_editable = ('DetPedDes', 'DetPedEstReg')
# Registrando los modelos con las configuraciones actualizadas
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Nutriente, NutrienteAdmin)
admin.site.register(Alimento, AlimentoAdmin)
admin.site.register(Toma, TomaAdmin)
admin.site.register(Dieta, DietaAdmin)
admin.site.register(Granja, GranjaAdmin)
admin.site.register(Proveedores, ProveedoresAdmin)
admin.site.register(Almacen, AlmacenAdmin)
admin.site.register(FechaInicio, FechaInicioAdmin)
admin.site.register(AnimalNutriente, AnimalNutrienteAdmin)
admin.site.register(DietaAnimalFechaInicio, DietaAnimalFechaInicioAdmin)
admin.site.register(NutrienteAlimento, NutrienteAlimentoAdmin)
admin.site.register(AlimentoDietaToma, AlimentoDietaTomaAdmin)
admin.site.register(Stock, StockAdmin)
admin.site.register(Ciudad, CiudadAdmin)
admin.site.register(Magnitud, MagnitudAdmin)
admin.site.register(Estado, EstadoAdmin)
admin.site.register(AnimalTipo, AnimalTipoAdmin)
admin.site.register(AnimalUtilidad, AnimalUtilidadAdmin)
admin.site.register(AlimentoTipo, AlimentoTipoAdmin)
admin.site.register(CabeceraPedido, CabeceraPedidoAdmin)
admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Pais, PaisAdmin)
admin.site.register(DetallesDePedido, DetallesDePedidoAdmin)
