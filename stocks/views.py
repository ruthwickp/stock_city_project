from django.shortcuts import render_to_response
from django.template import RequestContext

def index(request):
    context = RequestContext(request)
    context_dict = {'hello' : 'what'}
    return render_to_response('stocks/index.html', context_dict, context)
