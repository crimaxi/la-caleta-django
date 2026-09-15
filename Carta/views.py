from django.http import Http404
from django.shortcuts import render

PLATOS = [
    {"id": 1, "nombre": "Ceviche de reineta", "categoria": "Entrada", "precio": 8900,
     "tiempo": 10, "picante": True, "vegetariano": False,
     "descripcion": "Reineta fresca marinada en limon con cebolla morada, cilantro y aji verde."},
    {"id": 2, "nombre": "Empanadas de queso", "categoria": "Entrada", "precio": 4500,
     "tiempo": 15, "picante": False, "vegetariano": True,
     "descripcion": "Tres empanadas fritas de masa casera rellenas con queso mantecoso."},
    {"id": 3, "nombre": "Caldillo de congrio", "categoria": "Fondo", "precio": 12900,
     "tiempo": 25, "picante": False, "vegetariano": False,
     "descripcion": "Congrio dorado en caldo de verduras, papas y vino blanco. Receta de la casa."},
    {"id": 4, "nombre": "Pastel de choclo", "categoria": "Fondo", "precio": 9900,
     "tiempo": 30, "picante": False, "vegetariano": False,
     "descripcion": "Pino de carne, pollo, huevo y aceitunas cubierto con pasta de choclo gratinada."},
    {"id": 5, "nombre": "Porotos granados", "categoria": "Fondo", "precio": 7900,
     "tiempo": 20, "picante": False, "vegetariano": True,
     "descripcion": "Porotos frescos con zapallo, choclo y albahaca. Plato de temporada."},
    {"id": 6, "nombre": "Chorrillana", "categoria": "Fondo", "precio": 11900,
     "tiempo": 20, "picante": True, "vegetariano": False,
     "descripcion": "Papas fritas con carne salteada, cebolla, huevo y aji verde. Para compartir."},
    {"id": 7, "nombre": "Leche asada", "categoria": "Postre", "precio": 3900,
     "tiempo": 5, "picante": False, "vegetariano": True,
     "descripcion": "Postre tradicional de leche, huevo y caramelo, horneado y servido frio."},
    {"id": 8, "nombre": "Mote con huesillo", "categoria": "Postre", "precio": 2900,
     "tiempo": 5, "picante": False, "vegetariano": True,
     "descripcion": "Duraznos deshidratados cocidos en almibar con mote de trigo. Se sirve helado."},
]



def inicio(request):
    precio_promedio = round(sum(plato['precio'] for plato in PLATOS) / len(PLATOS))
    cantidad_vegetarianos = sum(1 for plato in PLATOS if plato['vegetariano'])
    contexto = {
        'platos': PLATOS,
        'precio_promedio': precio_promedio,
        'cantidad_vegetarianos': cantidad_vegetarianos,
    }
    return render(request, 'Carta/inicio.html', contexto)


def detalle(request, id):
    plato = None
    for plato_candidato in PLATOS:
        if plato_candidato['id'] == id:
            plato = plato_candidato
            break

    if plato is None:
        raise Http404('El plato no existe.')

    precio_con_propina = round(plato['precio'] * 1.10)
    if plato['vegetariano'] and not plato['picante']:
        etiqueta = 'Apto para todos'
    elif plato['picante']:
        etiqueta = 'Contiene aji'
    else:
        etiqueta = 'Plato tradicional'

    contexto = {
        'plato': plato,
        'precio_con_propina': precio_con_propina,
        'etiqueta': etiqueta,
    }
    return render(request, 'Carta/detalle.html', contexto)
