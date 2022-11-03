from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>")