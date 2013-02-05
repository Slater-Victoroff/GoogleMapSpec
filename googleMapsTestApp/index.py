from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context

def basicMap(request):
	return HttpResponse(get_template('basicMap.html').render(Context()))
