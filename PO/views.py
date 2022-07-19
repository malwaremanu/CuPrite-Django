from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import PO
from masters.models import Party

from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt 
def index(request):

    db = [ x.show_all() for x in PO.objects.all() ]
    if request.method == 'POST':
        print('method post')
        body = json.loads(request.body.decode('utf-8'))

        db = PO()
        # p_uuid=models.UUIDField(primary_key = True, default = uuid.uuid4)
        # p_no = models.CharField(max_length = 200,unique = True)
        # p_date = models.DateTimeField()
        # p_from_company = models.TextField()
        # po_supplier = models.ForeignKey('masters.Party', on_delete=models.CASCADE)
        # p_is_active = models.BooleanField()
        # p_tva_percentage = models.IntegerField()

        db.p_no = body["p_no"]
        db.p_date = body["p_date"]
        db.p_from_company = body["p_from_company"]
        db.po_supplier = Party.objects.get(p_uuid = body["po_supplier"])
        db.p_is_active = body["p_is_active"]
        db.p_no = body["p_no"]
        db.p_tva_percentage = body["p_tva_percentage"]
        db.save()

        return JsonResponse({
            "msg" : "all good.",
            "body" : body
        })
    
    return JsonResponse({
            "msg" : "all good.",
            "orders" : db
        })

@csrf_exempt 
def listall(request):
    db = PO.objects.all()
    print(db)
    context = {
        "data" : [ x.show_all() for x in db]
    }
    return JsonResponse(context)
