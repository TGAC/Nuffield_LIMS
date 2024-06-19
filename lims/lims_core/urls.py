from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:sample_id>/', views.sample_detail, name='sample_detail'),
    path('extraction/<int:extraction_id>/', views.sample_extraction, name='sample_extraction'),
]