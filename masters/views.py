from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import Party
import json
from .serial import partySerial 

from rest_framework.parsers import JSONParser


from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer



# Create your views here.
@csrf_exempt 
def index(request):
    return JsonResponse(
        {
            "msg" : "master's landing page."
        }
    )


# class partyViewSet(viewsets.ModelViewSet):
#     queryset = Party.objects.all().order_by('-p_date')
#     serializer_class = partySerial
#     # permission_classes = [permissions.IsAuthenticated]


# @csrf_exempt 
# def parties(request):
#     db = Party.objects.all()
#     print(db)
#     serializer = partySerial(db, many=True)
    
#     # context = {
#     #     "data" : [ x.show_all() for x in db]
#     # }

#     if request.method == 'POST':
#         print('method post')
#         body = json.loads(request.body.decode('utf-8'))

#         try:
#             db = Party()    

#             # "party_name": "Mita Locks Pvt Ltd",
#             # "party_email": "test@mitalocks.com",
#             # "p_address": "VKI India",
#             # "p_author": "manupal",
#             # "p_date": "2022-07-18T09:43:31Z",
#             # "p_company": "Suryamines",
#             # "p_is_active": true

#             db.p_author = "manupal"
#             db.p_name = body["p_name"]
#             db.p_email = body["p_email"]
#             db.p_address = body["p_address"]
#             db.p_is_active = body["p_is_active"]
#             #db.save()

#             return JsonResponse({
#                 "msg" : "all good.",
#                 "body" : body,
#                 "db" : str(db.show_all())
#             })
#         except:
#             return JsonResponse({
#                  "msg" : "error posting data"
#             })
       

#     if request.method == 'DELETE':
#         print('method DELETE')
#         body = json.loads(request.body.decode('utf-8'))

#         db = Party.objects.get(p_uuid=body["uuid"])   
#         db.delete()

#         return JsonResponse({
#             "msg" : "success"
#         })      

#     return JsonResponse(serializer.data, safe=False)

@api_view(('GET','PUT', 'POST', 'DELETE'))
#@renderer_classes((TemplateHTMLRenderer, JSONRenderer))
@csrf_exempt
def party_detail(request, pk=None):
    """
    Retrieve, update or delete a party snippet.
    """
    # try:
    #     if pk !=None:
    #         snippet = Party.objects.get(p_uuid=pk)
    #     else:
    #         snippet = Party.objects.create()
    # except Party.DoesNotExist:
    #     snippet = Party.objects.create()
    #     #return HttpResponse(status=404)





    if request.method == 'GET':
        if pk:                
            try:
                snippet = Party.objects.get(p_uuid=pk)
                serializer = partySerial(snippet)
            except Party.DoesNotExist:
                return HttpResponse(status=404)
        else:
            serializer = partySerial(Party.objects.all(), many=True)

        return Response(serializer.data)

    if request.method == 'DELETE':
        try: 
            snippet = Party.objects.get(p_uuid=pk)
            snippet.delete()
            return Response({"msg" : "Deleted Successfully."})
        except Party.DoesNotExist:
            return Response({"msg" : "UUID not found"})

    if request.method == 'POST':
        print('method POST')
        snippet = Party.objects.create()
        serializer = partySerial(snippet, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    
        return Response({
            "msg" : "please send valid data",
            "data" : [
                'p_name',
                'p_address',
                'p_author',
                'p_email',
                'p_company',
                'p_is_active'
            ]
            # {
            #         "p_name": "",
            #         "p_address": "",
            #         "p_author": "",
            #         "p_email": "hi@manupal.dev",
            #         "p_company": "suryamines",
            #         "p_is_active": true
            #     }
        })


    if request.method == 'PUT':
        print('method PUT')
        try:
            snippet = Party.objects.get(p_uuid=pk)
        except Party.DoesNotExist:
            return HttpResponse(status=404)
            
        serializer = partySerial(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            
        return Response(serializer.errors, status=400)
