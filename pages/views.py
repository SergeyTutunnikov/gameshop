from django.shortcuts import render
from products.models import Game
from django.views.generic import ListView 
# Create your views here.
def home_page(request):
    return render(request,'home.html')

class ShopPage(ListView):
    template_name="shop.html"
    model=Game
    context_object_name="games"
