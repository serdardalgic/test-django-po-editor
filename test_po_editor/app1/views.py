from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils.translation import pgettext, ugettext as _

# Create your views here.

month = pgettext("month name", "May")


def index(request):
    return_str = _("Hello from app1<br>")
    return_str = ("{}<br>").format(month)
    return_str += _('<a href="{}">Back to main page</a>').format(reverse('index'))
    return HttpResponse(return_str)
