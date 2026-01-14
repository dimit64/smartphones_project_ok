from django.db import models
# Create your models here.
from django.utils import timezone
# Πίνακας για τους Κατασκευαστές (π.χ. Apple, Samsung)
class Manufacturer(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
#Πίνακας λειτουργικό σύστημα
class OS(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
#Πίνακας κατασκευαστή επεξεργαστή
class CpuManufacturer(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
#Πίνακας δίκτυο σύνδεσης
class Network(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name

#Το κινητό (κυριο μοντέλο με τα δεδομένα)
class Mobile(models.Model):
    name=models.CharField(max_length=30)
#Σχέσεις - foreign keys
    Manufacturer=models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    OS=models.ForeignKey(OS,on_delete=models.CASCADE)
    CpuManufacturer=models.ForeignKey(CpuManufacturer,on_delete=models.CASCADE)
    Network=models.ForeignKey(Network,on_delete=models.CASCADE)
#Μεταδεδομένα - Χαρακτηριστικά
    screen_type=models.CharField(max_length=30)
    screen_size=models.DecimalField(max_digits=4,decimal_places=2)
    ram=models.PositiveIntegerField
    storage=models.PositiveIntegerField
    cores=models.PositiveIntegerField
    price=models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return f"{self.manufacturer.name} {self.name}"


