# iihave created this file -- jayvanjare
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello')

    
def about(request):
    return HttpResponse('About')