from django.shortcuts import render
from .data_models import ticket,ticketForm
# Create your views here.
def indexview(request):
    return render(request,'santorini/index.html')

def loginview(request):
    return render(request,'santorini/login.html')

def dashboardview(request):
    return render(request,'santorini/dashboard.html')

def ticketview(request):
    create_form = ticketForm()
    context={"form":create_form}
    if request.method== 'POST':
        create_form = ticketForm(request.POST)
        if create_form.is_valid():
            create_form.save()
    return render(request,'santorini/report_ticket.html',context)
    