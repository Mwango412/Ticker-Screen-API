from django.db import models
    
class commodityname(models.model):
    commodityname = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class commodity_Prices(models.model):
     commodity_prices= models.IntegerField()
    
def __str__(self):
        return self.price
    

