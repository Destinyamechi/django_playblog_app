from django.shortcuts import render
from rest_framework import generics , status
from rest_framework.generics import GenericAPIView
from rest_framework.views import Response
from order.models import Order
from . serializers import *
from dj_rest_auth.registration.views import RegisterView

# Create your views here.
class customerRegisterView(RegisterView):
    serializer_class = customerRegisterSerializer



# placing an order
class customerOrderView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = placeOrderSerializer

    def post(self, request):
        serializer = placeOrderSerializer(data= request.data)
        if serializer.is_valid(raise_exception= True):
            serializer.save(customer = self.request.user.customer)
            return Response(serializer.data)
        return Response(serializer.errors)


# all the orders
class orderView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = placeOrderSerializer



# getting a particular order
class singleOrderView(GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = placeOrderSerializer
    def get(self, request, orderId):
        order = Order.objects.filter(customer = self.request.user.customer).get(order_id = orderId)
        serializer = placeOrderSerializer(order,many = False)
        return Response(serializer.data)
    
    def put(self, request, orderId):
        order = Order.objects.filter(customer = self.request.user.customer).get(order_id = orderId)
        serializer = placeOrderSerializer(instance=order, data = request.data, partial = True)
        if serializer.is_valid(raise_exception= True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def delete(self, request, orderId):
        order = Order.objects.filter(customer = self.request.user.customer).get(order_id = orderId)
        order.delete()
        return Response({'message: The order has been deleted'}, status=status.HTTP_204_NO_CONTENT)


class tierAndModesView(GenericAPIView):
    queryset = Mode.objects.all()
    serializer_class = modeSerializer
    def get(self, request):
        tier = Mode.objects.all()
        serializer = modeSerializer(tier, many = True)
        return Response(serializer.data)

    

    
    
