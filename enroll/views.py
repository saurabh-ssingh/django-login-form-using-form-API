from django.shortcuts import render
from enroll.forms import LoginForm
from enroll.models import User
# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        fm=LoginForm(request.POST)
        if fm.is_valid():
           
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            rpw=fm.cleaned_data['rpassword']
            reg=User(name=nm,email=em,password=pw,rpassword=rpw)
            reg.save()
    else:
            fm=LoginForm()    
    
    return render(request,'enroll/loginform.html',{'form':fm})

