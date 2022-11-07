from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index_html_test, name='index'),
    path('all', views.product_list_view, name='all'),
    path('<int:pk>', views.product_detail_view, name='all'),
]
