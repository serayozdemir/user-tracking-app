from django.http import JsonResponse

def log_list(request):
    # Örnek bir view fonksiyonu
    data = {"message": "Log listesi çalışıyor!"}
    return JsonResponse(data)