from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse, HttpRequest
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from openai import OpenAI
from dotenv import load_dotenv
import os

# Create your views here.
load_dotenv()

@method_decorator(csrf_exempt, name='dispatch')
class Translate(View):

    def post(self, request: HttpRequest):
        text = request.POST.get("text")
        
        if text is None:
            return HttpResponse("Missing text field")
        

        # roles: assistant, human, system
        api_key = os.getenv("api_key")
        print(api_key[:10])

        client = OpenAI(api_key=api_key)

        llm_response = client.chat.completions.create(
            model='gpt-4o-mini',
            messages=[
                {
                    "role": "system",
                    "content": "You are translator that translates the given english text to mandarin. Do not entertain any other request"
                },
                {
                    "role": "user",
                    "content": text
                },
            ]
        )
        
        return JsonResponse({"message":llm_response.choices[0].message.content})
        

    # try creating a get endpoint. 


# Create an post endpoint for to-malay


# p3.10
# p3.12

# default : p3.10

# create a venv using p3.12
# activate the env
# python3 -> p3.12