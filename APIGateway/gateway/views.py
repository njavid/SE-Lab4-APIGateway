from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from .models import Data
from django.core.cache import cache


@csrf_exempt
def index(request):
#    del request.session['fail_counter']

    print("start")
    
    stop =  cache.get('stop')
    print(stop)
    counter = request.session.get('fail_counter')

    if counter is None:
        counter = 0
    
    if stop is None:
        try:
            external_api_url = 'http://127.0.0.1:3000/here/'
            data = request.POST
            res = requests.post(external_api_url, data, timeout=0.5)

        except Exception as e:
            print("counter :",counter % 3)
            counter += 1
            if counter % 3 == 0:
                print("hererer")
                cache.set('stop', 'stop', 30)

            request.session['fail_counter'] = counter
            print("Timeout", counter)
    else:
        print("NOT availble")

    
    
    print("success")
    
    return HttpResponse("Hello, world. You're at the gateway index.")