
from django.shortcuts import render
from rest_framework.views import APIView
from .models import commodityname,commodity_Prices
from rest_framework import Serializers
from ticker import LED_display
import json from commodity
import requests
import time
from ..CommodityTicker import commodity

class FetchCommodityData(APIView):
    def get(self, request):
        while True:
            response = requests.get('http://api.zamace.co.zm/daily/commodities/prices')
            data = response.json()

            for commodity in data['commodities']:
                display_message = f"{commodity['name']}: {commodity['price']}"

                #led_display = LED_display()
                #led_display.send(display_message)

               # print(display_message)

            time.sleep(1800)  

print(commodity)