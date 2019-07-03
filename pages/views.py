from django.template import loader
from django.http import HttpResponse
from .models import advertisement
from .models import Comments

from .models import AD_pics
from django.utils import timezone
import json

def Buy(request):
    template = loader.get_template('Game/index.html')
    return HttpResponse(template.render())  # template.render(page_data, request))
