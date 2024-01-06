from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import Customer
from order.models import Order
from company.models import *

                     #------- create serializers here ---------#

# overriding dj-rest-auth register serializer to implement other attributes of the customer
class customerRegisterSerializer(RegisterSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    age = serializers.CharField(required = True)
    address = serializers.CharField(required = True)
    phone_number = serializers.CharField(required = True)

    def get_cleaned_data(self):
        data = super(customerRegisterSerializer, self).get_cleaned_data()
        extra_data = {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'age':self.validated_data.get('age'),
            'address':self.validated_data.get('address'),
            'phone_number':self.validated_data.get('phone_number')

        }
        data.update(extra_data)
        return data
    
    def save(self, request):
        user = super(customerRegisterSerializer, self).save(request)
        user.save()
        customer = Customer(
            user = user,
            first_name = self.cleaned_data.get('first_name'),
            last_name = self.cleaned_data.get('last_name'),
            age = self.cleaned_data.get('age'),
            address = self.cleaned_data.get('address'),
            phone_number = self.cleaned_data.get('phone_number')
        )
        customer.save()
        return user



# PLACE ORDER SERIALIZER #
class placeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ('customer', 'order_id',)



# check all the Tiers and Modes
class tierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tier
        fields = ("tier_level", "bio",)


class modeSerializer(serializers.ModelSerializer):
    tier = tierSerializer(many = True)
    class Meta:
        model = Mode
        fields = ('mode_name', 'bio', 'tier',)
        read_only_fields = ('id',)

