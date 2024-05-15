from django.shortcuts import redirect, render
from . models import actor
from . forms import actorForm
# Create your views here.

def home(request):
    if request.POST:
     frm=actorForm(request.POST,request.FILES)
     
     if frm.is_valid():
            frm.save()
            return redirect ('list')
    else:
        frm=actorForm()

    return render(request,"index.html",{'frm':frm})

def list(request):
    lit=actor.objects.all()
    return render(request,"list.html",{'lit':lit})

def edited(request,pk):
    edt = actor.objects.get(pk=pk)
    if request.POST:
        frm = actorForm(request.POST,request.FILES,instance=edt)
        if frm.is_valid():
            edt.save()

            return redirect('list')

    else:
        frm = actorForm(instance=edt)
        print(frm)


    return render(request,"edit.html",{'frm':frm})

def delete(request,pk):
    delt=actor.objects.get(pk=pk)
    delt.delete()
    lit=actor.objects.all()

    return render(request,'list.html',{'lit':lit})
    



