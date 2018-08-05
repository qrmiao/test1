from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin

from stu.models import Student

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 统一验证登录
        # return None 或者不写
        if request.path == '/stu/login/' or request.path == '/stu/regist/':
            return None

        ticket = request.COOKIES.get('ticket')
        if  ticket:
            users = Student.objects.filter(s_ticket=ticket)
            if users:
                request.user = users
                return None
            else:
                return HttpResponseRedirect('/stu/login/')
        return HttpResponseRedirect('/stu/login/')








