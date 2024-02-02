from django.urls import path
from.views import commodity_prices

urlpatterns =[
    path ('commodity_prices/',commodity_prices, name='commodity_prices')
]
