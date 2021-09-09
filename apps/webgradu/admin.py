from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class resourceemisor(resources.ModelResource):
    class Meta:
        model = emisor

class adminemisor(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['apellido', 'phone', 'comprob']
    resource_class = resourceemisor

admin.site.register(emisor, adminemisor)


class resourcereceptor(resources.ModelResource):
    class Meta:
        model = receptor

class adminreceptor(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['apellido', 'phone', 'guia']
    resource_class = resourcereceptor

admin.site.register(receptor, adminreceptor)

class resourcemensajero(resources.ModelResource):
    class Meta:
        model = mensajero
class adminmensajero(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['id_mensajero']
    list_display = ['name', 'apellido','phone', 'correo']
    resource_class = resourcemensajero

admin.site.register(mensajero, adminmensajero)

class resourcepaquete(resources.ModelResource):
    class Meta:
        model = paquete

class adminpaquete(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['guia']
    list_display = ['descrip', 'ubication', 'peso', 'tipo']
    resource_class = resourcepaquete

admin.site.register(paquete, adminpaquete)

class resourceseguimiento(resources.ModelResource):
    class Meta:
        model = seguimiento

class adminseguimiento(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['fecha']
    list_display = ['ubicacion', 'estado']
    resource_class = resourceseguimiento

admin.site.register(seguimiento, adminseguimiento)

