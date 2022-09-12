from django.shortcuts import render,redirect

from sampleapp.forms import StudentForm
from sampleapp.models import Student

# Create your views here.
def crud(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid:
            form.save()
    form=StudentForm()
    obj=Student.objects.all()
    template_name='index.html'
    context={'form':form,'obj':obj}
    return render(request,template_name,context)

def delete(request,id):
    obj=Student.objects.get(id=id)
    obj.delete()
    return redirect('home')

def update(request,id):
    obj=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=obj)
        if form.is_valid:
            form.save()
            return redirect('home')
    form=StudentForm(instance=obj)
    template_name="update.html"
    context={'form':form}
    return render(request,template_name,context)