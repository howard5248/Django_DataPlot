from django.urls import path,include
from . import views

urlpatterns = [
    path('selectSt/',views.selectSt,name='selectSt'),
    # path('plotSt/',views.plotSt,name='plotSt'),
    # path('test/',views.test,name='test'),
]