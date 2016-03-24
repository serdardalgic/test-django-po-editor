from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.utils.translation import ugettext as _

# Create your views here.


def index(request):
    return_str = _("Hello from app2<br>")
    return_str += _('<a href="{}">Back to main page</a>').format(reverse('index'))
    return HttpResponse(return_str)
