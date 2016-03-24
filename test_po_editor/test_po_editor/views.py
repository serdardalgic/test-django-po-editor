from django.core.urlresolvers import reverse
from django.http import HttpResponse


def index(request):
    return_str = "Please select the app to go:<br>"
    return_str += '<a href="{}">app1</a><br>'.format(reverse('app1'))
    return_str += '<a href="{}">app2</a><br>'.format(reverse('app2'))
    return HttpResponse(return_str)
