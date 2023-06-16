from django.db.models.query import RawQuerySet
from django.shortcuts import redirect, render
from .models import Student
from django.contrib import messages

# Create your views here.

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        query = Student(name=name, email=email, age=age, gender=gender)
        query.save()
        messages.success(request, "Data inserted successfully")
        return redirect('index')
        
    data = Student.objects.all()
    context = {
        'students': data,
    }
    return render(request, 'index.html', context)



def delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.error(request, "Data deleted successfully")
    return redirect("/")


def update(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        age = request.POST['age']
        gender = request.POST['gender']
        student = Student.objects.get(id=id)
        student.name = name
        student.email = email
        student.age = age
        student.gender = gender
        student.save()
        messages.warning(request, "Data updated successfully")
        return redirect("/")

    student = Student.objects.get(id=id)
    return render(request, 'edit.html', {'std':student})