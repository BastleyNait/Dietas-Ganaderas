from django.shortcuts import render
from django.db import connection
from .models import Granja
from .forms import GranjaForm
def todosLospedidos(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM recibo1")
        rows = cursor.fetchall()
        context = []
        for row in rows:
            context.append({
                'producto': row[11],
                'precio': row[12],
            })

        """
        productos = []
        precios = []
        for row in rows:
            productos.append(row[11])
            precios.append(row[12])

        # for row in rows:
            # print(row[11])  

    # Procesar los datos si es necesario antes de pasar al contexto
    context = {
        'productos': productos, 
        'precios': precios,
    }
        
        """
    return render(request, 'reporte.html', 
                  {'items':context})


def consulta_directa_view(request, id):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM recibo1 WHERE CabPedCod = {id}")
        rows = cursor.fetchall()
        items = []
        for row in rows:
            items.append({
                'producto': row[11],
                'precio': row[12],
            })
        total = 0
        for row in rows:
            total = total + row[12]
        print(total)
        datos = {
            'codigo': rows[0][0],
            'proveedor': rows[0][1],
            'codAlmacen': rows[0][2],
            'granja': rows[0][3],
            'empresa': rows[0][4],
            'fecha': rows[0][8],
            'hora': rows[0][9],
            'descripcion': rows[0][10],
            'total': total,
        }

    return render(request, 'reporte.html', {
                      'items':items,
                      'datos':datos,
                   })

def gestion_granjas(request):
    granjas = Granja.objects.all()

    return render(request, 'granjas.html', {
        'granjas': granjas,
        'form': GranjaForm,
    })

    