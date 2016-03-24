from django.core.urlresolvers import reverse
from django.http import HttpResponse

# Create your views here.

def index(request):
    return_str = "Hello from app1<br>"
    return_str += '<a href="{}">Back to main page</a>'.format(reverse('index'))
    return HttpResponse(return_str)
