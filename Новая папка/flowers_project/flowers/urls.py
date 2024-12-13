from django.urls import path
from . import views

urlpatterns = [
    path('flowers/', views.all_flowers, name='all_flowers'),
    path('flowers/type/<int:type_id>/', views.flowers_by_type, name='flowers_by_type'),
    path('flowers/<int:flower_id>/', views.flower_detail, name='flower_detail'),
]
