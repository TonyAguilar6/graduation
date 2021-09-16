from django.db import models

# Create your models here.
class emisor(models.Model):
    pk_emisor = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=8, null=False, blank=False)
    comprob = models.CharField(max_length=9, null=False, blank=False)

    class Meta:
        verbose_name = 'emisor'
        verbose_name_plural = 'emisor'
        ordering = ['name']

    def __str__(self):
        return "{0}".format(self.name)


class receptor(models.Model):
    pk_receptor = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=8, null=False, blank=False)
    guia = models.CharField(max_length=9, null=False, blank=False)

    class Meta:
        verbose_name = 'receptor'
        verbose_name_plural = 'receptor'
        ordering = ['name']

    def __str__(self):
        return "{0}".format(self.name)


class mensajero(models.Model):
    ps_mensajero= models.AutoField(primary_key=True, null=False, blank=False)
    id_mensajero = models.CharField(max_length=5, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    apellido = models.CharField(max_length=50, null=False, blank=False)
    phone = models.CharField(max_length=8, null=False, blank=False)
    correo = models.CharField(max_length=40, null=False, blank=False)

    class Meta:
        verbose_name = 'mensajero'
        verbose_name_plural = 'mensajero'
        ordering = ['name']

    def __str__(self):
        return "{0}".format(self.name)


class paquete(models.Model):
    pk_paquete = models.AutoField(primary_key=True, null=False, blank=False)
    guia = models.CharField(max_length=9, null=False, blank=False)
    descrip = models.TextField(null=False, blank=False)
    ubication = models.CharField(max_length=80, null=False,blank=False)
    peso = models.DecimalField(null=False, max_digits=2, decimal_places=2)
    tipo = models.TextField(null=False,blank=False)
    image = models.URLField(max_length=800, default='https://i.postimg.cc/vTphDsSm/undraw-warning-cyit.png', blank=False, null=False)
    fk_emisor = models.ForeignKey(emisor, null=False, blank=False, on_delete=models.CASCADE)
    fk_receptor = models.ForeignKey(receptor, null=False, blank=False, on_delete=models.CASCADE)
    fk_mensajero = models.ForeignKey(mensajero, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'paquete'
        verbose_name_plural = 'paquete'
        ordering = ['guia']

    def __str__(self):
        return "{0}".format(self.guia)


class seguimiento(models.Model):
    pk_seguimiento  = models.AutoField(primary_key=True, null=False, blank=False)
    fecha = models.CharField(max_length=8, null=False, blank=False)
    ubicacion = models.TextField(max_length=80, null=False,blank=False)
    estado = models.TextField(max_length=2, null=False,blank=False)
    fk_paquete = models.ForeignKey(paquete, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'seguimiento'
        verbose_name_plural = 'seguimiento'
        ordering = ['ubicacion']

    def __str__(self):
        return "{0}".format(self.ubicacion)



