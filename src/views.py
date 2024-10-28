from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def informasi_pribadi(request):
    return render(request, 'informasi_pribadi.html')

def pendidikan(request):
    return render(request, 'pendidikan.html')

def keterampilan(request):
    return render(request, 'keterampilan.html')

def kontak(request):
    return render(request, 'kontak.html')
