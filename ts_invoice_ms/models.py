from django.db import models

# Create your models here.

class Invoice(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.BigIntegerField('Id usuario', unique=True, default='null')
    producto = models.IntegerField('Código Producto', unique=True, default='null')
    factura_fecha= models.DateTimeField('Fecha de compra',auto_now_add=True,blank=True)
    direccion_envio = models.CharField('Direccion de envío', max_length = 80, unique=False, default='null')
    metodo_pago = models.CharField('Método de pago', max_length = 20, unique=False, default='null')
    valor_envio = models.IntegerField('Balor de envío', unique=False, default='null')
    valor_producto = models.IntegerField('Valor de producto', unique=False, default='null')
    valor_impuesto = models.IntegerField('Valor de impuesto',  unique=False, default='null')
    subtotal = models.IntegerField('Subtotal',  unique=False, default='null')
    valor_total = models.IntegerField('Valor total', unique=False, default='null')