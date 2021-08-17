from django.shortcuts import render


# Create your views here.
def perfumes(request):
    context = {}
    return render(request, 'perfumes/index.html', context)



def checkout(request):
      context = {}
      return render(request, 'perfumes/checkout.html', context)