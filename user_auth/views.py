from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt 
def index(request):

    return JsonResponse({
        "msg" : "user to be authenticated"
    })

@csrf_exempt 
def login(request):
    try:
        body = json.loads(request.body.decode('utf-8'))
        username = body["username"]
        password = body["password"]

        load_db = open("user.db")
        ldb = [ x.strip().split(',') for x in load_db.readlines() ]
        
        check_db = [username, password]    
        request.session['username'] = username
        request.session['password'] = password
            
        return JsonResponse({
            "msg" : "Login Successfull" if check_db in ldb else "Wrong Username or Password"
        })

    except:
        return JsonResponse({
            "msg" : "did you forgot to send username or password ?"
        })

@csrf_exempt 
def logout(request):
    try:
        del request.session['username']
        del request.session['password']
    except:
        pass
    return JsonResponse({
        "msg" : "user logged out"
    })

@csrf_exempt 
def status(request):
    if request.session:
        status = True
    else:
        status = False

    return JsonResponse({
        "status" : status
    })