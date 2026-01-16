from django.shortcuts import render

# Create your views here.
from .models import Mobile

def mobile_list(request):
    mobiles = Mobile.objects.all()
    return render(request, 'catalog/mobile_list.html', {'mobiles': mobiles})
