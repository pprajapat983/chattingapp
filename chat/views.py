from django.shortcuts import render,redirect
from .models import Message

# Create your views here.
def home(request):
    if request.method=='POST':
        msg=request.POST.get('msg')
        name=request.user
        newmsg=Message(msg=msg,name=name)
        newmsg.save()
        return redirect('home')
    message=Message.objects.all()
    return render(request,'chat/home.html',{'message': message})

