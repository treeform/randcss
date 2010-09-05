from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")
    
def design(request):
    return HttpResponse("Hello, world.")
    
def style(request):
    return HttpResponse("Hello, world.")    
