from django.db import models


class Stock(models.Model):
    """ Class describes a stock and contains many fields providing
    information about it. """

    ask_price = IntegerField()
    todays_range = CharField(max_length=20)
    todays_high = IntegerField()
    todays_low = IntegerField()
    volume = IntegerField()



                