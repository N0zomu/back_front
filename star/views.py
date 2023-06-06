from django.shortcuts import render
import json
from star.models import Star
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def add_star(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        user_id = data_json['user_id']
        book_id = data_json['book_id']
    
        star = Star(user_id=user_id, book_id=book_id)
        
        star.save()
        return JsonResponse({'result': 1, 'message': '添加成功'})

@csrf_exempt
def delete_star(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        user_id = data_json['user_id']
        book_id = data_json['book_id']
        
        try:
            star = Star.objects.get(user_id=user_id,book_id=book_id)
            star.delete()
            return JsonResponse({'result': 1, 'message': '删除成功'})
        except Star.DoesNotExist:
            return JsonResponse({'result': 0, 'message': '收藏不存在'})

@csrf_exempt
def list_star(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        user_id = data_json['user_id']
        
        stars = Star.objects.filter(user_id__icontains=user_id)
        
        star_list = []
        for star in stars:
            star_data = {
                'star_id': star.id,
                'user_id': star.user_id,
                'book_id': star.book_id,
            }
            star_list.append(star_data)
        
        return JsonResponse({'result': 1, 'message': '查询成功', 'stars': star_list})