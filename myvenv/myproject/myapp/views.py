from django.shortcuts import render, redirect
from .models import Powder, Container, Cap, Bag, Water, Tray
from django.db.models import Sum
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def production(request):
    return render(request, 'production.html')

def dovegel(request):
    return render(request, 'dovegel.html')

def inventory(request):
    return render(request, 'inventory.html')

def products(request):
    return render(request, 'products.html')

def rawmaterials(request):
    powders = Powder.objects.all()
    containers = Container.objects.all()
    caps = Cap.objects.all()

    total_powder = sum(powder.quantity for powder in powders)
    
    total_containers = {
        '500g': sum(container.quantity for container in containers if container.size == '500g'),
        '700g': sum(container.quantity for container in containers if container.size == '700g'),
        '300g': sum(container.quantity for container in containers if container.size == '300g'),
    }

    total_caps = {
        '500g': sum(cap.quantity for cap in caps if cap.size == '500g'),
        '700g': sum(cap.quantity for cap in caps if cap.size == '700g'),
        '300g': sum(cap.quantity for cap in caps if cap.size == '300g'),
    }

    return render(request, 'rawmaterials.html', {
        'powders': powders,
        'containers': containers,
        'caps': caps,
        'total_powder': total_powder,
        'total_containers': total_containers,
        'total_caps': total_caps,
    })

def add_powder(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        quantity = float(request.POST.get('quantity'))
        Powder.objects.create(location=location, quantity=quantity)
    return redirect('rawmaterials')
    

def add_container(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity'))
        Container.objects.create(company_name=company_name, size=size, quantity=quantity)
    return redirect('rawmaterials')
    
def add_cap(request):
    if request.method == 'POST':
        company_name = request.POST.get('company_name')
        size = request.POST.get('size')
        quantity = int(request.POST.get('quantity'))
        Cap.objects.create(company_name=company_name, size=size, quantity=quantity)
    return redirect('rawmaterials')

def rawmaterials_view(request):
    # Store entered data
    if request.method == "POST":
        if "bag_submit" in request.POST:
            company_name = request.POST.get("company_name")
            count = int(request.POST.get("count"))
            Bag.objects.create(company_name=company_name, count=count)

        if "water_submit" in request.POST:
            date = request.POST.get("date")
            liters = float(request.POST.get("liters"))
            Water.objects.create(date=date, liters=liters)

        if "tray_submit" in request.POST:
            date = request.POST.get("date")
            quantity = int(request.POST.get("quantity"))
            Tray.objects.create(date=date, quantity=quantity)

        return redirect("rawmaterials")

    # Fetch totals
    total_bags = Bag.objects.aggregate(Sum("count"))["count__sum"] or 0
    total_water = Water.objects.aggregate(Sum("liters"))["liters__sum"] or 0
    total_trays = Tray.objects.aggregate(Sum("quantity"))["quantity__sum"] or 0

    # Fetch all records for display
    bags = Bag.objects.all()
    water_records = Water.objects.all()
    tray_records = Tray.objects.all()

    return render(request, "rawmaterials.html", {
        "total_bags": total_bags,
        "total_water": total_water,
        "total_trays": total_trays,
        "bags": bags,
        "water_records": water_records,
        "tray_records": tray_records,
    })