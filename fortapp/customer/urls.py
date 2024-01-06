from django.urls import path
from . views import *
from dj_rest_auth.views import LoginView

urlpatterns = [
    path('customerregister/', customerRegisterView.as_view()),
    path('placeorder/', customerOrderView.as_view()),
    path('get/<str:orderId>/', singleOrderView.as_view()),
    path('order/', orderView.as_view()),
    path('tier/', tierAndModesView.as_view()),
]