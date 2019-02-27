from django.shortcuts import render
from .models import Products

# Create your views here.
def product_view(request):
    obj = Products.objects.get(id = 1)
    contex = {
        "object": obj
    }
    return render(request, "product/details.html", contex)
