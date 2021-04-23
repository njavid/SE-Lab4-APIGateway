from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests
from django.core.cache import cache

@csrf_exempt
def register(request):
    stop =  cache.get('stop')

    counter = request.session.get('fail_counter')

    if counter is None:
        counter = 0
    
    response_data = {}
    if stop is None:

        try:
            received_json_data = json.loads(request.body)
            
            request_type = "POST"
            api_url = 'http://127.0.0.1:3000/register/'
            response = requests.request(request_type, api_url, data=json.dumps(received_json_data), timeout=0.5)
        

            print("status=",response.status_code)
            if response.status_code == 201:
                response_data['message'] = 'created successfully'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=201)
            elif response.status_code == 400:
                response_data['message'] = 'username exists!'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=400)
            else:
                response_data['message'] = 'method not allowed'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=405)



        except Exception as e:
            counter += 1
            if counter % 3 == 0:
                cache.set('stop', 'stop', 30)

            request.session['fail_counter'] = counter

            response_data['message'] = 'Timeout! Please try again.'
            return HttpResponse(json.dumps(response_data), content_type="application/json", status=408)

    else:
        response_data['message'] = 'Service not available'
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=503)


def login(request):
    stop =  cache.get('stop')

    counter = request.session.get('fail_counter')

    if counter is None:
        counter = 0
    
    response_data = {}
    if stop is None:
        try:
            received_json_data = json.loads(request.body)
            
            request_type = "GET"
            api_url = 'http://127.0.0.1:3000/login/'
            response = requests.request(request_type, api_url, data=json.dumps(received_json_data), timeout=0.5)
        

            if response.status_code == 200:
                response_data['message'] = 'logged in successfully'
                response_data['token'] = json.loads(response.text)['token']
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
            elif response.status_code == 401:
                response_data['message'] = 'username or password incorrect!'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=401)
            else:
                response_data['message'] = 'method not allowed'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=405)



        except Exception as e:
            print(e)
            counter += 1
            if counter % 3 == 0:
                cache.set('stop', 'stop', 30)

            request.session['fail_counter'] = counter

            response_data['message'] = 'Timeout! Please try again.'
            return HttpResponse(json.dumps(response_data), content_type="application/json", status=408)

    else:
        response_data['message'] = 'Service not available'
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=503)


def profile(request):
    stop =  cache.get('stop')

    counter = request.session.get('fail_counter')

    if counter is None:
        counter = 0

    response_data = {}

    if stop is None:
        try:

            request_type = "GET"
            api_url = 'http://127.0.0.1:3000/profile/'
            response = requests.request(request_type, api_url, headers=request.headers, timeout=0.5)

            if response.status_code == 201:
                data = json.loads(response.text)

                return HttpResponse(json.dumps(data), content_type="application/json", status=201)
            elif response.status_code == 400:
                response_data['message'] = 'Invalid token. Please log in again.'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=400)
            else:
                response_data['message'] = 'method not allowed'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=405)



        except Exception as e:
            print("eror",e)
            counter += 1
            if counter % 3 == 0:
                cache.set('stop', 'stop', 30)

            request.session['fail_counter'] = counter

            response_data['message'] = 'Timeout! Please try again.'
            return HttpResponse(json.dumps(response_data), content_type="application/json", status=408)

    else:
        response_data['message'] = 'Service not available'
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=503)
    
@csrf_exempt
def update(request):
    stop =  cache.get('stop')

    counter = request.session.get('fail_counter')

    if counter is None:
        counter = 0
    
    response_data = {}
    if stop is None:
        try:
            received_json_data = json.loads(request.body)

            data = {}
            if "username" in received_json_data:
                data["username"] = received_json_data["username"]
            if "password" in received_json_data:
                data["password"] = received_json_data["password"]
            if "email" in received_json_data:
                data["email"] = received_json_data["email"]
            if "mobile" in received_json_data:
                data["mobile"] = received_json_data["mobile"]

            request_type = "POST"
            api_url = 'http://127.0.0.1:3000/update/'
            response = requests.request(request_type, api_url,data=json.dumps(data), headers=request.headers, timeout=0.5)

            if response.status_code == 200:
                response_data['message'] = 'updated successfully.'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
            else:
                response_data['message'] = 'method not allowed'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=405)



        except Exception as e:
            print("eror",e)
            counter += 1
            if counter % 3 == 0:
                cache.set('stop', 'stop', 30)

            request.session['fail_counter'] = counter

            response_data['message'] = 'Timeout! Please try again.'
            return HttpResponse(json.dumps(response_data), content_type="application/json", status=408)

    else:
        response_data['message'] = 'Service not available'
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=503)
 

def isAdmin(token):
    request_type = "POST"
    api_url = 'http://127.0.0.1:3000/identify/'
    response = requests.request(request_type, api_url, data=json.dumps({'token':token}), timeout=0.5)
    res = json.loads(response.text)
    if res['admin']:
        return True
    else:
        return False


@csrf_exempt
def createBook(request):
    stop =  cache.get('stop')

    counter = request.session.get('fail_counter')

    if counter is None:
        counter = 0
    
    response_data = {}

    if stop is None:
        try:
            received_json_data = json.loads(request.body)

            admin = isAdmin(received_json_data['token'])

            print(admin)

            if admin :
                request_type = "POST"
                api_url = 'http://127.0.0.1:8000/create/'
                response = requests.request(request_type, api_url, data=json.dumps(received_json_data), timeout=0.5)

                print("helllskllkfesndc")

                if response.status_code == 201:
                    return HttpResponse(json.dumps({'message' : response.text}), content_type="application/json", status=201)
                else:
                    response_data['message'] = 'method not allowed'
                    return HttpResponse(json.dumps(response_data), content_type="application/json", status=405)
            else:
                response_data['message'] = 'Not allowed for clients'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=405)


        except Exception as e:
            print(e)
            counter += 1
            if counter % 3 == 0:
                cache.set('stop', 'stop', 3)

            request.session['fail_counter'] = counter

            response_data['message'] = 'Timeout! Please try again.'
            return HttpResponse(json.dumps(response_data), content_type="application/json", status=408)

    else:
        response_data['message'] = 'Service not available'
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=503)

@csrf_exempt
def updateBook(request):
    stop =  cache.get('stop')

    counter = request.session.get('fail_counter')

    if counter is None:
        counter = 0
    
    response_data = {}
    if stop is None:
        try:
            received_json_data = json.loads(request.body)

            admin = isAdmin(received_json_data['token'])

            if admin:

                request_type = "POST"
                api_url = 'http://127.0.0.1:8000/update/'
                response = requests.request(request_type, api_url,data=json.dumps(received_json_data), headers=request.headers, timeout=0.5)

                if response.status_code == 200:
                    response_data['message'] = 'updated successfully.'
                    return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
                elif response.status_code == 400:
                    response_data['message'] = 'book id please.'
                    return HttpResponse(json.dumps(response_data), content_type="application/json", status=400)

                else:
                    response_data['message'] = 'method not allowed'
                    return HttpResponse(json.dumps(response_data), content_type="application/json", status=405)
            else:
                response_data['message'] = 'Not allowed for clients'
                return HttpResponse(json.dumps(response_data), content_type="application/json", status=405)



        except Exception as e:
            print("eror",e)
            counter += 1
            if counter % 3 == 0:
                cache.set('stop', 'stop', 30)

            request.session['fail_counter'] = counter

            response_data['message'] = 'Timeout! Please try again.'
            return HttpResponse(json.dumps(response_data), content_type="application/json", status=408)

    else:
        response_data['message'] = 'Service not available'
        return HttpResponse(json.dumps(response_data), content_type="application/json", status=503)

# @csrf_exempt
# def deleteBook(request):
#     stop =  cache.get('stop')

#     counter = request.session.get('fail_counter')

#     if counter is None:
#         counter = 0
    
#     response_data = {}
#     if stop is None:
#         try:
#             received_json_data = json.loads(request.body)

#             request_type = "POST"
#             api_url = 'http://127.0.0.1:8000/delete/'
#             response = requests.request(request_type, api_url,data=json.dumps(received_json_data), headers=request.headers, timeout=0.5)

#             if response.status_code == 200:
#                 response_data['message'] = 'deleted successfully.'
#                 return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
#             elif response.status_code == 401:
#                 response_data['message'] = 'the book does not exists!'
#                 return HttpResponse(json.dumps(response_data), content_type="application/json", status=400)

#             else:
#                 response_data['message'] = 'method not allowed'
#                 return HttpResponse(json.dumps(response_data), content_type="application/json", status=405)



#         except Exception as e:
#             print("eror",e)
#             counter += 1
#             if counter % 3 == 0:
#                 cache.set('stop', 'stop', 30)

#             request.session['fail_counter'] = counter

#             response_data['message'] = 'Timeout! Please try again.'
#             return HttpResponse(json.dumps(response_data), content_type="application/json", status=408)

#     else:
#         response_data['message'] = 'Service not available'
#         return HttpResponse(json.dumps(response_data), content_type="application/json", status=503)

# @csrf_exempt
# def readBook(request):
#     print("here")
#     stop =  cache.get('stop')

#     counter = request.session.get('fail_counter')

#     if counter is None:
#         counter = 0
    
#     response_data = {}
#     if stop is None:
#         try:
#             received_json_data = json.loads(request.body)

#             request_type = "POST"
#             api_url = 'http://127.0.0.1:8000/read/'
#             response = requests.request(request_type, api_url,data=json.dumps(received_json_data), headers=request.headers, timeout=0.5)

#             if response.status_code == 200:
#                 print(json.loads(response.text))
            
#                 response_data = json.loads(response.text)
                
#                 return HttpResponse(json.dumps(response_data), content_type="application/json", status=200)
#             else:
#                 response_data['message'] = 'method not allowed'
#                 return HttpResponse(json.dumps(response_data), content_type="application/json", status=405)
#         except Exception as e:
#             print("eror",e)
#             counter += 1
#             if counter % 3 == 0:
#                 cache.set('stop', 'stop', 30)

#             request.session['fail_counter'] = counter

#             response_data['message'] = 'Timeout! Please try again.'
#             return HttpResponse(json.dumps(response_data), content_type="application/json", status=408)

#     else:
#         response_data['message'] = 'Service not available'
#         return HttpResponse(json.dumps(response_data), content_type="application/json", status=503)
        
