from rest_framework import serializers
from  .serializer import commodity

class commoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = commodity
        fields = '__all__'

class commodity_priceSerializer(serializers.ModelSerializer):
 class Meta:
     model=commodity
     fields ='_all_'