from django.shortcuts import render


def index(request):
    return render(request, 'global/pages/base.html')
