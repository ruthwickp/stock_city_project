from django.shortcuts import render_to_response
from django.template import RequestContext
from stocks.models import Stock
import ystockquote
import collections

def index(request):
    """ Home page displays list of all stocks. """
    context = RequestContext(request)
    context_dict = {'all_stocks' : Stock.objects.all()}
    return render_to_response('stocks/index.html', context_dict, context)

def stock(request, stock_symbol):
    """ Displays useful information pertaining to a single stock
    passed by the url link. """
    context = RequestContext(request)
    context_dict = {'stock_symbol' : stock_symbol}

    # Tries to find if stock with that symbol exists
    try:
        stock = Stock.objects.get(symbol=stock_symbol)
        context_dict['stock'] = stock
        # Adds dictionary of stock properties to context dict
        context_dict.update(stock_properties(stock))
    # Displays nothing, lets template display not found message
    except Stock.DoesNotExist:
        pass

    return render_to_response('stocks/stock.html', context_dict, context)

def stock_properties(stock):
    """ Retrieves properties for a given stock and returns a 
    dictionary containing it. """
    stock_dict = {}
    stock_dict['stock_name'] = stock.name
    stock_dict['stock_ask_realtime'] = ystockquote.get_ask_realtime(stock.symbol)
    stock_dict['stock_today_open'] = ystockquote.get_today_open(stock.symbol)
    stock_dict['stock_volume'] = ystockquote.get_volume(stock.symbol)
    stock_dict['stock_change'] = ystockquote.get_change(stock.symbol)
    stock_dict['stock_change_percent'] = ystockquote.get_change_percent(
        stock.symbol)[1:-1]
    stock_dict['stock_todays_range'] = ystockquote.get_todays_range(
        stock.symbol)[1:-1]

    # Gets past dates
    stock_dict['historical_prices_dict'] = collections.OrderedDict(
        sorted(eval(stock.historical_prices).items(), key=lambda t: t[0]))

    return stock_dict



