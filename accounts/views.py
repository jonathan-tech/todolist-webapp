from django.shortcuts import render,redirect
from django.contrib.auth.models import User #gives user object
from django.contrib import auth
# Create your views here.
def signup(request):
    #user is signing up
    if request.method=="POST":
        #lets check if pass1==pass2
        if request.POST['password1'] == request.POST['password2']:
            try:
                #check if username is taken
                user= User.objects.get(username=request.POST['username'])
                #display error in signup.html
                return render(request, 'accounts/signup.html',{'error':'username taken'})
            except User.DoesNotExist:
                #username is not taken, make the user account
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password2'])
                #login
                auth.login(request,user)
                #direct to create page
                return redirect('create')
        else:
            #password didnt match
            return render(request, 'accounts/signup.html',{'error':'passwords must match'})


    else:
        #just get to the page
        return render(request, 'accounts/signup.html')



def login(request):
    #user is signing up
    if request.method=="POST":
        #if authenticate gives a valid user object, meaning the account exist
        user=auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        #found your account
        if user is not None:
            #log user in
            auth.login(request,user)
            #direct to homepage
            return redirect('create')
        else:
            #the user typed in invalid info
            return render(request, 'accounts/login.html',{'error':'username or password inccorect'})
    else:
        #just get to page
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('home')
