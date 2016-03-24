from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils.translation import ugettext as _


def index(request):
    return_str = "Please select the app to go:<br>"
    return_str += '<a href="{}">app1</a><br>'.format(reverse('app1'))
    return_str += '<a href="{}">app2</a><br>'.format(reverse('app2'))
    # Translators: This is the main page
    output = _(return_str)
    return HttpResponse(output)
