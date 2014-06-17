from django.shortcuts import render_to_response
from django.template import RequestContext
from stocks.models import Stock
import ystockquote

def index(request):
    """ Home page displays list of all stocks """
    context = RequestContext(request)
    context_dict = {'all_stocks' : Stock.objects.all()}
    return render_to_response('stocks/index.html', context_dict, context)


