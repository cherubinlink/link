from django.shortcuts import render

# Create your views here.



def index(request):
    return render(request, 'service/index.html')



def marketing(request):
    return render(request, 'service/marketing.html')

def web(request):
    return render(request,'service/web.html')

def cloud(request):
    return render(request,'service/cloud.html')

def donne(request):
    return render(request,'service/donnes.html')