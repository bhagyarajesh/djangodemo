from django.shortcuts import render
from shop.models import Product
from django.db.models import Q
# Create your views here.
def searchproducts(request):
    p = None  # initialized to None
    query = ""
    if (request.method == "POST"):  # after form submission
        query = request.POST['q']
        if query:
            p = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))


    return render(request, 'search.html', {'pro': p, 'query': query})
