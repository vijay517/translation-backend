from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
class Translate(View):

    def post(self, request: HttpRequest):
        text = request.POST.get("text")
        
        if text is None:
            return HttpResponse("Missing text field")
        
        print(text)

        return JsonResponse({"message":"Translation complete"})
        

    # try creating a get endpoint. 


# Create an post endpoint for to-malay
    