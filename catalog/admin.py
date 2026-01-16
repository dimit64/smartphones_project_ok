from django.contrib import admin
from .models import Manufacturer, CpuManufacturer, OS, Network, Mobile

# Register your models here.
admin.site.register(Manufacturer)
admin.site.register(CpuManufacturer)
admin.site.register(OS)
admin.site.register(Network)
admin.site.register(Mobile)