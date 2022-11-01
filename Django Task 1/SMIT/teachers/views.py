from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello Teachers, welcome to SMIT!.</h1>")