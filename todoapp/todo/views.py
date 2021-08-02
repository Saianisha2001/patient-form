from todo.forms import patientform
from django.shortcuts import redirect, render

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from .models import Patient
def home(request):
    if request.method=='POST':
        pat=Patient()
        pat.fname=request.POST.get('fname')
        pat.lname=request.POST.get('lname')
        pat.gender=request.POST.get('gender')
        pat.age=request.POST.get('age')
        pat.disease=request.POST.get('disease')
        pat.docname=request.POST.get('docname')
        pat.docfee=request.POST.get('docfee')
        pat.save()
        all  = Patient.objects.all()   
        context = {
            'all': all
        }
        return render(request,'views.html',context)
    else:
        return render(request,'index.html')
def view(request):
    all  = Patient.objects.all()
    context = {
        'all': all,
    }
    return render(request,'views.html',context)

def delete(request,sno):
    all = Patient.objects.filter(sno=sno)
    all.delete()
    return redirect('view')



def edit(request, sno):
    task = get_object_or_404(Patient, pk = sno)
    if request.method == 'POST':
        form = patientform(request.POST, instance = task)
        if form.is_valid():
            task = form.save(commit = False)
            task.save()
            return redirect('view')
    else:
        form = patientform(instance = task)

    return render(request, template_name = 'update.html', context = { 'form': form })

    
