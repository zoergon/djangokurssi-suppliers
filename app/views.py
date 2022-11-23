from django.shortcuts import render

# lähettää selaimelle landingpagen
def landingview(request):
    return render(request, 'landingpage.html')

def productlistview(request):
    return render(request, 'productlist.html')

def supplierlistview(request):
    return render(request, 'supplierlist.html')

