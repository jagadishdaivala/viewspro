from django.http import HttpResponse

def welcome(request):
    return HttpResponse("<h1 style='color : red'>Hello</h1>")