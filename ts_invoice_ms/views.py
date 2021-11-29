from django.shortcuts import render

# Create your views here.

from rest_framework import status, views
from rest_framework.response import JsonResponse
from rest_framework.parsers import JSONParser
from ts_invoice_ms.models import Invoice
from ts_invoice_ms.serializers import InvoiceSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def invoice_list(request):
    if request.method == 'GET':
        facturas = Invoice.objects.all()            
        facturas_serializer = InvoiceSerializer(facturas, many=True)
        return JsonResponse(facturas_serializer.data, safe=False)
        
    elif request.method == 'POST':
        factura_data = JSONParser().parse(request)
        factura_serializer = InvoiceSerializer(data=factura_data)
        if factura_serializer.is_valid():
            factura_serializer.save()
            return JsonResponse(factura_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(factura_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Invoice.objects.all().delete()
        return JsonResponse({'message': '{} facturas fueron borradas exitosamente'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def factura_detail(request, pk):
    try: 
        factura = Invoice.objects.get(pk=pk) 
    except Invoice.DoesNotExist: 
        return JsonResponse({'message': 'No existe esa factura'}, status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET': 
        factura_serializer = InvoiceSerializer(factura)
        return JsonResponse(factura_serializer.data) 

    elif request.method == 'PUT': 
        factura_data = JSONParser().parse(request) 
        factura_serializer = InvoiceSerializer(factura, data=factura_data) 
        if factura_serializer.is_valid(): 
            factura_serializer.save() 
            return JsonResponse(factura_serializer.data) 
        return JsonResponse(factura_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    elif request.method == 'DELETE': 
        factura.delete() 
        return JsonResponse({'message': 'La factura fue borrada'}, status=status.HTTP_204_NO_CONTENT)