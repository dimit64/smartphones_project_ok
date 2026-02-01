from django.shortcuts import render, get_object_or_404
from .models import Mobile
from django.utils import timezone
from django.db.models import Q
# Create your views here.

def index(request):
    mobiles = Mobile.objects.all()
    return render(request, 'catalog/index.html')


def mobile_list(request):
    brand_id = request.GET.get('brand', '').strip()
    txt=request.GET.get('txt', '').strip()
    mobiles = Mobile.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    if brand_id:
        mobiles = mobiles.filter(Manufacturer_id=brand_id)
    else:
        if txt:
            mobiles = mobiles.filter(
                (Q(name__icontains=txt) | Q(review__icontains=txt) |Q(Manufacturer__name__icontains=txt) | Q(ram__icontains=txt) & Q(published_date__lte=timezone.now())
            ))
            mobiles = mobiles.order_by('published_date')

    return render(request, 'catalog/mobile_list.html', {'mobiles': mobiles})


def mobile_detail(request, pk):
    mobile = get_object_or_404(Mobile, pk=pk)
    return render(request, 'catalog/mobile_detail.html', {'mobile': mobile})

def about_us(request):
    return render(request, 'catalog/about.html')