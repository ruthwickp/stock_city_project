from django.contrib import admin
from stocks.models import Stock

class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')

admin.site.register(Stock, StockAdmin)