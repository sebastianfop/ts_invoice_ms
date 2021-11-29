from ts_invoice_ms.models import Invoice
from rest_framework import serializers

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id','user','producto','factura_fecha','direccion_envio',
        'metodo_pago','valor_envio','valor_producto','valor_impuesto','subtotal','valor_total']