from django.shortcuts import render
import json
from user.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def register(request):
    if request.method == 'POST':
        print("POST")
        return JsonResponse({'result': 1, 'message': '注册成功!'})