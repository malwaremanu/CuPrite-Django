from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Party
import json

# Create your views here.
@csrf_exempt 
def index(request):
    return JsonResponse(
        {
            "msg" : "master's landing page."
        }
    )

@csrf_exempt 
def parties(request):
    db = Party.objects.all()
    print(db)
    context = {
        "data" : [ x.show_all() for x in db]
    }

    if request.method == 'POST':
        print('method post')
        body = json.loads(request.body.decode('utf-8'))

        try:
            db = Party()    

            # "party_name": "Mita Locks Pvt Ltd",
            # "party_email": "test@mitalocks.com",
            # "p_address": "VKI India",
            # "p_author": "manupal",
            # "p_date": "2022-07-18T09:43:31Z",
            # "p_company": "Suryamines",
            # "p_is_active": true

            db.p_author = "manupal"
            db.p_name = body["p_name"]
            db.p_email = body["p_email"]
            db.p_address = body["p_address"]
            db.p_is_active = body["p_is_active"]
            #db.save()

            return JsonResponse({
                "msg" : "all good.",
                "body" : body,
                "db" : str(db.show_all())
            })
        except:
            return JsonResponse({
                 "msg" : "error posting data"
            })

    if request.method == 'PUT':
        print('method PUT')
        body = json.loads(request.body.decode('utf-8'))

        try:
                
            db = Party.objects.get(p_uuid=body["uuid"])                       
            db.p_author = "manupal"
            db.p_name = body["p_name"]
            db.p_email = body["p_email"]
            db.p_address = body["p_address"]
            db.p_company = body["p_company"]
            db.p_is_active = body["p_is_active"]
            db.save()

            return JsonResponse({
                "msg" : "all good.",
                "body" : body,
                "db" : str(db.show_all())
            })
        
        except:
            return JsonResponse({
                "msg" : "error updating"
            })

    if request.method == 'DELETE':
        print('method DELETE')
        body = json.loads(request.body.decode('utf-8'))

        db = Party.objects.get(p_uuid=body["uuid"])   
        db.delete()

        return JsonResponse({
            "msg" : "success"
        })      

    return JsonResponse(context)