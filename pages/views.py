from django.http import HttpResponse

def home(request):
    return HttpResponse('для Искандера: 8=====D')