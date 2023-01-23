from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

def emp(request):
    if request.method == "POST":
        employees = EmployeeForm(request.POST)
        if employees.is_valid():
            try:
                employees.save()
                return redirect('/restapp/show')
            except:
                pass
    else:
        employees = EmployeeForm()
    return render(request,'index.html',{'employees':employees})

def show(request):
    dataset = Employee.objects.all()
    return render(request,"show.html",{'dataset':dataset})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, 'edit.html', {'employee': employee})

def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/restapp/show")

