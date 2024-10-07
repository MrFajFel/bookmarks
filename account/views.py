from django.shortcuts import render

from account.form import Loginform

def user_login(request):
    if request.method == "POST":
        pass
    else:
        form = Loginform()
    return  render(request,'account/login.html',{'form': form})


# Create your views here.
