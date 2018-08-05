from django.http import HttpResponseRedirect

from stu.models import Student


def is_login(func):
    def chenckout_login(request):
        ticket = request.COOKIES.get('ticket')
        if ticket:
            users = Student.objects.filter(s_ticket=ticket)
            if users:
                return func(request)
            else:
                return HttpResponseRedirect('/stu/login/')
        else:
            return HttpResponseRedirect('/stu/login/')
    return chenckout_login