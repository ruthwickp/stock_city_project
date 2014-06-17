from django.db import models


class Stock(models.Model):
    """ Class describes a stock and contains fields providing
    information about it. """
    symbol = models.CharField(max_length=10)   
    name = models.CharField(max_length=50)
    historical_prices = models.TextField(max_length=None)


    def __unicode__(self):
        """ Returns the symbol of the stock as a string when method
        is called. """
        return self.name