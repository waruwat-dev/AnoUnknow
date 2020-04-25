from django.shortcuts import render

def not_found(request):
    return render(request, 'not_found.html')