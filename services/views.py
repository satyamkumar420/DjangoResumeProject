from django.shortcuts import render

# Create your views here.


def service(request):
    context = {'services': 'active'}

    return render(request, 'services/services.html', context)
