from django.shortcuts import render
import json
from label.models import Label
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def add_label(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        user_id = data_json['user_id']
        book_id = data_json['book_id']
        chapter_id = data_json['chapter_id']
        cfi = data_json['cfi']
        percentage = data_json['percentage']
        time = data_json['time']
        
        label = Label(user_id=user_id, book_id=book_id, chapter_id=chapter_id, cfi=cfi, percentage=percentage, time=time)
        label.save()
        
        return JsonResponse({'result': 1, 'message': '添加成功'})
    
@csrf_exempt
def delete_label(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        label_id = data_json['id']
        
        try:
            label = Label.objects.get(id=label_id)
            label.delete()
            return JsonResponse({'result': 1, 'message': '删除成功'})
        except Label.DoesNotExist:
            return JsonResponse({'result': 0, 'message': '标签不存在'})
        
@csrf_exempt
def edit_label(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        label_id = data_json['id']
        user_id = data_json['user_id']
        book_id = data_json['book_id']
        chapter_id = data_json['chapter_id']
        cfi = data_json['cfi']
        percentage = data_json['percentage']
        time = data_json['time']
        
        try:
            label = Label.objects.get(id=label_id)
            label.user_id = user_id
            label.book_id = book_id
            label.chapter_id = chapter_id
            label.cfi = cfi
            label.percentage = percentage
            label.time = time
            label.save()
            return JsonResponse({'result': 1, 'message': '编辑成功'})
        except Label.DoesNotExist:
            return JsonResponse({'result': 0, 'message': '标签不存在'})

@csrf_exempt
def search_label(request):
    if request.method == 'POST':
        data_json = json.loads(request.body)
        
        user_id = data_json['user_id']
        book_id = data_json['book_id']
        chapter_id = data_json['chapter_id'] 
        
        try:
            label = Label.objects.get(user_id=user_id, book_id=book_id, chapter_id=chapter_id)
        
            label_data = {
                'label_id': label.id,
                'user_id': label.user_id,
                'book_id': label.book_id,
                'chapter_id': label.chapter_id,
                'cfi': label.cfi,
                'percentage': label.percentage,
                'time': label.time.strftime('%Y-%m-%d %H:%M:%S') if label.time else None
            }
            
            return JsonResponse({'result': 1, 'message': '查询成功', 'labels': label_data})
        except Label.DoesNotExist:
            return JsonResponse({'result': 0, 'message': '未找到匹配的标签'})