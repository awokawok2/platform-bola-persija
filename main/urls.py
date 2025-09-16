from django.urls import path
from main.views import show_main, create_product, show_product

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-news/', create_product, name='create_news'),
    path('news/<str:id>/', show_product, name='show_news'),
]
