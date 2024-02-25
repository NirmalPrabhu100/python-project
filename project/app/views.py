from django.shortcuts import render,redirect
from app import views
from app.form import pyclass
from app.models import tableone

def onefun (request):
    if request.method=='POST':
        F=pyclass(request.POST)
        if F.is_valid():
            F.save()
        return redirect('twofun')
    else:
        F=pyclass()
        return render(request,template_name='one.html', context = {'form' : F})
    
def twofun (request):

    x = tableone.objects.all().values()
    return render(request,template_name='sucess.html', context = {'val' : x} )