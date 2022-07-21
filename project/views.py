from django.http import JsonResponse
from django.shortcuts import redirect, render
import os, datetime
import json

def server_restart(request):
    os.system('pip install -r requirements.txt')
    os.system("echo '' > tmp/restart.txt")
    context = {
        'msg' : 'success', 
        'git' : 'updated', 
        'time' : str(datetime.datetime.now())
    }    
    return JsonResponse(context)