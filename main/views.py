from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app' : 'Platform Bola Persija',
        'name': 'Raditya Amoret',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)