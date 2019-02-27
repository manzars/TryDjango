from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello World!</h1>")
    my_contex = {
        "my_name": "manzar",
        "my_number": 9167121589,
        "my_age": [123,564,656,76454,1416, 'abc']
    }
    return render(request, "home.html", my_contex)

def contacts_view(request, *args, **kwargs):
    print(request.user)
    #return HttpResponse("<h1>Contact Pages!</h1>")
    
    return render(request, "contact.html", {})
