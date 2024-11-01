from django.shortcuts import render,HttpResponse

# Diccionario de módulos 
MODULOS = {
    1: 'Admision',
    2: 'Equipos',
    3: 'Recargas',
    4: 'Creditos',
    5: 'Cobranzas',
    6: 'Liquidacion',
    7: 'Reporteria',

}

def modulo(request, numero):
    nombre_modulo = MODULOS.get(numero, 'Módulo Desconocido')
    return render(request, f'modulo{numero}/modulo{numero}.html', {'numero': numero, 'nombre_modulo': nombre_modulo})

# En views.py
def tu_vista(request):
    modulos = [{'nombre': 'Admision', 'url': 'modulo', 'numero': 1},
               {'nombre': 'Equipos', 'url': 'modulo', 'numero': 2},
               {'nombre': 'Recargas', 'url': 'modulo', 'numero': 3},
               {'nombre': 'Creditos', 'url': 'modulo', 'numero': 4},
               {'nombre': 'Cobranzas', 'url': 'modulo', 'numero': 5},
               {'nombre': 'Liquidacion', 'url': 'modulo', 'numero': 6},
               {'nombre': 'Reporteria', 'url': 'modulo', 'numero': 7},


              ]
    return render(request, 'app/index.html', {'modulos': modulos})


