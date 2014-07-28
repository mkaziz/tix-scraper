
## Django imports
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

## Python imports
import json

def createJSONResponse(data):
    response_data = { "success" : True, "data" : data }
    return HttpResponse(content=json.dumps(response_data), content_type="application/json")

# Create your views here.
def index(request):
    #return createJSONResponse({})
    return getPrices(request)

# Create your views here.
def getPrices(request, eventId=None):
    if eventId == None:
        return render(request, "index.html")
    
    render(request, "index.html", {something: "hello world"})