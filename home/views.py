from django.shortcuts import render, HttpResponse
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Contact
# Create your views here.
def index(request):
    return render(request,"index.html")
    # return HttpResponse("Hello")
# def contact(request):
#     if request.method=='POST':
#         contact=Contact(name= request.POST.get('name'),email=request.POST.get('email'),phone=request.POST.get('phone'),message=request.POST.get('message'))
#         contact.save()

#         messages.success(request,"Message sent successfully!")
#         return HttpResponseRedirect('/')    


def contact(request):
    if request.method=='POST':
        name=request.POST['name']   
        email=request.POST['email']   
        phone=request.POST['phone']   
        content=request.POST['content'] 
        # print(name,email,phone,content)  
        contact=Contact(name=name,email=email,phone=phone,message=content)
        contact.save()
    return render(request,'index.html')    