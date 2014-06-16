from django.db import models


class Stock(models.Model):
    """ Class describes a stock and contains many fields providing
    information about it. """
    symbol = models.CharField(max_length=10, unique=True)   
    name = models.CharField(max_length=50, unique=True)
    ask_realtime = models.FloatField()
    todays_range = models.CharField(max_length=40)
    volume = models.FloatField()


    def __unicode__(self):
        """ Returns the symbol of the stock as a string when method
        is called. """
        return self.name