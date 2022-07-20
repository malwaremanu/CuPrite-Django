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
        
        
        if check_db in ldb:
            request.session['username'] = username
            msg = "Login Successfull"
        else:
            msg = "Wrong Username or Password"

        return JsonResponse({
            "msg" :  msg
        })

    except:
        return JsonResponse({
            "msg" : "did you forgot to send username or password ?"
        })

@csrf_exempt 
def logout(request):
    try:
        request.session.flush()
        # del request.session['username']
    except:
        pass
    return JsonResponse({
        "msg" : "user logged out"
    })

@csrf_exempt 
def status(request):
    print(request.session)
    if request.session.get('username', False):
        status = True
    else:
        status = False

    return JsonResponse({
        "status" : status
    })