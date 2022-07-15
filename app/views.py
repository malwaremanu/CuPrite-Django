from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Choo Choo! This is your Django app 🚅")

def api(request):
    context = {
        "name" : 'Manupal'
    }

    return JsonResponse(context)