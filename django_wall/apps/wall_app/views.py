from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from .models import User, Message, Comment

def index(request):
    return render(request, "wall_app/index.html")
# Create your views here.

def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        hpwd = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=request.POST["fname"],last_name=request.POST["lname"],password=hpwd,email=request.POST["email"])
        request.session['use'] = request.POST["fname"]
        return redirect("/wall")

def login(request):
    errors = User.objects.pw_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        name = User.objects.filter(email=request.POST["email"])
        request.session['use'] = name[0].first_name
        print(name[0].first_name)
        return redirect("/wall")

def welcome(request):
    return render(request, "wall_app/welcome.html")

def logout(request):
    request.session.clear()
    return redirect("/")
    
def show(request):
    print(User.objects.all().values())
    return redirect("/")

def delete(request):
    c=User.objects.all()
    c.delete()
    print(User.objects.all().values())
    return redirect("/")

    #---------wall code
def wall(request):
    if 'use' not in request.session:
        return redirect("/")
    context = {
        "posts":Message.objects.all().order_by("-created_at"),
        "comments":Comment.objects.all().order_by("-created_at")
    }
    return render(request,"wall_app/wall.html",context)

def post_message(request):
    text = request.POST["message"]
    uid = User.objects.get(first_name=request.session['use']).__dict__
    Message.objects.create(message=text, creator_id=uid['id'])
    return redirect("/wall")

def post_comment(request):
    text = request.POST["comment"]
    cid = User.objects.get(first_name=request.session['use']).__dict__
    print(text, cid['id'], request.POST["pid"])
    Comment.objects.create(comment=text, commenter_id=cid['id'], commment_message=Message.objects.get(id=request.POST["pid"]))
    return redirect("/wall")

def delete_post(request, my_val):
    d=Comment.objects.filter(commment_message=int(my_val))
    d.delete()
    c=Message.objects.get(id=int(my_val))
    c.delete()
    return redirect("/wall")