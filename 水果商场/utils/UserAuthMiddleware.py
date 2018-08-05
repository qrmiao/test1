from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.core.urlresolvers import reverse
from user.models import UserTicketModel
import re
from axf02 import settings

from datetime import datetime, timedelta


class UserMiddleware(MiddlewareMixin):


    def process_request(self, request):
        if request.path == '/user/login' or request.path == '/user/register'or request.path == '/app/home'or request.path == '/app/market/':
            return None
        # if re.match('/app/market/(\d+)/(\d+)/(\d+)/',request.path):
        #     return None
        ticket = request.COOKIES.get('ticket')

        if not ticket:
           return HttpResponseRedirect(reverse('user:login'))

        user = UserTicketModel.objects.filter(ticket=ticket).first()
        if not user:
            return HttpResponseRedirect(reverse('user:login'))
        if user.out_time.replace(tzinfo=None)<datetime.now():
            user.delete()
            return HttpResponseRedirect(reverse('user:login'))
        request.user=user.user


