from django.shortcuts import render, redirect
from .models import Visitor
from visitorsapp.form import VisitorForm

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        mobile_number = request.POST.get('mobile_number')
        Visitor.objects.create(name=name, address=address, mobile_number=mobile_number)
        return redirect('index')

    visitors = Visitor.objects.all()
    return render(request, 'apps/index.html', {'visitors': visitors})

def delete(request,id):
	value=Visitor.objects.get(id=id)
	value.delete()
	return redirect('index')

def update(request,id):
	value=Visitor.objects.get(id=id)
	if request.method=="POST":
		form=VisitorForm(request.POST,instance=value)
		if form.is_valid():
			form.save()
		return redirect('index')
	return render(request,'apps/update.html',{'v':value})			
