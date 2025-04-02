from django.db import models

class Powder(models.Model):
    LOCATION_CHOICES = [
        ('kolathur', 'Kolathur'),
        ('bangalore', 'Bangalore'),
    ]
    location = models.CharField(max_length=20, choices=LOCATION_CHOICES)
    quantity = models.PositiveIntegerField(default=0)  # In grams
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.company_name} - {self.location} - {self.quantity}g"

class Container(models.Model):
    SIZE_CHOICES = [
        ('500g', '500g'),
        ('700g', '700g'),
        ('300g', '300g'),
    ]
    company_name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.company_name} - {self.size} - {self.quantity}"

class Cap(models.Model):
    company_name = models.CharField(max_length=100)
    size = models.CharField(max_length=10, choices=[('500g', '500g'), ('700g', '700g'), ('300g', '300g')])
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.company_name} - {self.size} - {self.quantity}"
    
class Bag(models.Model):
    company_name = models.CharField(max_length=255)
    count = models.PositiveIntegerField()

class Water(models.Model):
    date = models.DateField(auto_now_add=True)
    liters = models.PositiveIntegerField()

class Tray(models.Model):
    date = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField()