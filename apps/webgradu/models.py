from django.db import models

# Create your models here.
class emisor(models.Model):
    pk_emisor = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=8, null=False, blank=False)
    comprob = models.CharField(max_length=9, null=False, blank=False)


class receptor(models.Model):
    pk_receptor = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=8, null=False, blank=False)
    guia = models.CharField(max_length=9, null=False, blank=False)

class mensajero(models.Model):
    ps_mensajero= models.AutoField(primary_key=True, null=False, blank=False)
    id_mensajero = models.CharField(max_length=5, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=8, null=False, blank=False)
    correo = models.CharField(max_length=40, null=False, blank=False)

class paquete(models.Model):
    pk_paquete = models.AutoField(primary_key=True, null=False, blank=False)
    guia = models.CharField(max_length=9, null=False, blank=False)
    descrip = models.TextField(null=False, blank=False)
    ubication = models.CharField(max_length=80, null=False,blank=False)
    peso = models.DecimalField(null=False, max_digits=2, decimal_places=2)
    tipo = models.TextField(null=False,blank=False)
    fk_emisor = models.ForeignKey(emisor, null=False, blank=False, on_delete=models.CASCADE)
    fk_receptor = models.ForeignKey(receptor, null=False, blank=False, on_delete=models.CASCADE)
    fk_mensajero = models.ForeignKey(mensajero, null=False, blank=False, on_delete=models.CASCADE)

class seguimiento(models.Model):
    pk_seguimiento  = models.AutoField(primary_key=True, null=False, blank=False)
    fecha = models.CharField(max_length=8, null=False, blank=False)
    ubicacion = models.TextField(max_length=80, null=False,blank=False)
    estado = models.TextField(max_length=2, null=False,blank=False)
    fk_paquete = models.ForeignKey(paquete, null=False, blank=False, on_delete=models.CASCADE)


