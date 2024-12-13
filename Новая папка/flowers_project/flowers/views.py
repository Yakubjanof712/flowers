from django.shortcuts import render, get_object_or_404
from .models import Type, Flower

def all_flowers(request):
    flowers = Flower.objects.all()
    return render(request, 'flowers/all_flowers.html', {'flowers': flowers})

def flowers_by_type(request, type_id):
    type_obj = get_object_or_404(Type, id=type_id)
    flowers = type_obj.flowers.all()
    return render(request, 'flowers/flowers_by_type.html', {'type': type_obj, 'flowers': flowers})

def flower_detail(request, flower_id):
    flower = get_object_or_404(Flower, id=flower_id)
    return render(request, 'flowers/flower_detail.html', {'flower': flower})
