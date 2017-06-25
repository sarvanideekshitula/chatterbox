from django.shortcuts import render

# Create your views here.
from login.models import Registration


def register(request,ak):
    if request.method == "POST":
        Firstname = request.POST.get('firstname')
        Lastname = request.POST.get('lastname')
        Username = request.POST.get('username')
        Password = request.POST.get('password')
        Dateofbirth = request.POST.get('date')
        u = Registration.objects.create(firstname=Firstname,lastname=Lastname,username=Username,password=Password,dateofbirth=Dateofbirth)
        u.save()
        return render(request,'login/success.html',{})
    model = Registration
    object_list = Registration.objects.get(id=ak)
    print(object_list)

    context = {'object_list':object_list}
    return render(request,'login/registration.html',context)

def login(request,ak):
    if request.method == "POST":
        if Registration.objects.filter(username=request.POST['username'],password=request.POST['password']).exists():
            return render(request, 'login/success.html', {})
        else :
            return render(request, 'login/new.html', {})
    model = Registration
    object_list = Registration.objects.get(id=ak)
    return render(request, 'login/login.html', {})