from django.shortcuts import render, redirect
from .models import Clients


def displayindex(request):
    return render(request, "index.html")


def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        idnum = request.POST.get('idnum')
        address = request.POST.get('address')
        housenum = request.POST.get('housenum')
        contact = request.POST.get('contact')
        payment = request.POST.get('payment')

        submit_data = Clients(name=name, idnum=idnum, address=address, housenum=housenum, contact=contact, payment=payment)
        submit_data.save()
        return redirect("/")
    return render(request, "records.html")


def index(request):
    data = Clients.objects.all()
    context = {"data" : data}
    return render(request, "index.html", context)

def deleteData(request, id):
    d = Clients.objects.get(id=id)
    d.delete()
    return redirect("/records")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        idnum = request.POST.get('idnum')
        address = request.POST.get('address')
        housenum = request.POST.get('housenum')
        contact = request.POST.get('contact')
        payment = request.POST.get('payment')

        edit = Clients.objects.get(id=id)
        edit.name = name
        edit.idnum = idnum
        edit.address = address
        edit.housenum = housenum
        edit.contact = contact
        edit.payment = payment
        edit.save()
        return redirect('/')
    d = Clients.objects.get(id=id)
    context ={"d" :d}
    return render(request, "edit.html", context)

def records(request):
    data = Clients.objects.all()
    context = {"data": data}

    return render(request, 'records.html', context)

def update(request):
    data = Clients.objects.all()
    context = {"data": data}

    return render(request, 'edit.html', context)

def editpage(request):
    return render(request, 'edit.html')
# def recordspage(request):
#     return render(request, 'records.html')
