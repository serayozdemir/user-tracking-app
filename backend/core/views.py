# core/views.py
from django.http import HttpResponse
from django.urls import path

def example_view(request):
    return HttpResponse("Bu bir örnek sayfadır!")

# core/urls.py
urlpatterns = [
    path('', example_view),
]