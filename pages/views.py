from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from django.contrib.auth import login


# Create your views here.

#render main html(base.html) file
user="LOGIN"
def index_view(request,*args,**kwrgs):
    global user

    if request.method =="POST":

        log_form=AuthenticationForm(data=request.POST)
        print(log_form.is_valid())
        if log_form.is_valid():           
            user=log_form.get_user()
            login(request,user)
            print(user)
            print("0000000000000000000000000000000000000")
            #login_name=request.POST[username]
            
            return redirect('/')
            
        
    log_form=AuthenticationForm()
    context={
        "log_form":log_form,
        "name":user
    }
            
    return render(request,'template/index/index.html',context)






def about_view(request,*args,**kwrgs):
    return render(request,'template/index/about.html')


def contact_view(request,*args,**kwrgs):
    return render(request,'template/index/contact.html')





def reg_success_view(request,*args,**kwrgs):

    if request.method =="POST":
            Reg_form=UserCreationForm(request.POST)
                
            if Reg_form.is_valid():

                Reg_form.save() 
                return redirect('/')
    Reg_form=UserCreationForm()
    context={
        "Reg_form":Reg_form
    }

    return render(request,'template/index/reg_success.html',context)