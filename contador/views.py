from django.http import JsonResponse
from django.shortcuts import render
from .models import Contador

def index(request):
    return render(request, 'contador/index.html')

def registrar_valor(request):
    if request.method == 'POST':
        valor = request.POST.get('valor', '').strip()

        if valor:
            contador, created = Contador.objects.get_or_create(valor=valor)
            contador.contagem += 1
            contador.save()

            return JsonResponse({'valor': valor, 'contagem': contador.contagem - 1})
        return JsonResponse({'error': 'Valor inválido'}, status=400)

    return JsonResponse({'error': 'Método não permitido'}, status=405)
