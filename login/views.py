from django.shortcuts import render

# Create your views here.
from login.models import Registration


def register(request):
    if request.method == "POST":
        Firstname = request.POST.get('firstname')
        Lastname = request.POST.get('lastname')
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        Dateofbirth = request.POST.get('date')
        u = Registration.objects.create(firstname=Firstname,lastname=Lastname,username=Username,password=Password,dateofbirth=Dateofbirth)
        u.save()
        content = {'myvar': Registration.objects.latest('id')}
        return render(request,'login/success.html',content)
    model = Registration
    return render(request,'login/registration.html',{})

def login(request):
    if request.method == "POST":
        if Registration.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            return render(request, 'login/success.html', {})
        else :
            return render(request, 'login/new.html', {})
    model = Registration
    return render(request, 'login/login.html', {})
