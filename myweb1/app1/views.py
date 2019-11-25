from django.shortcuts import render

# Create your views here.

from django.views.generic import View
from . import models

class Login(View):
    def get(self, request):
        return render(request, 'app1/login_form.html')

    def post(self, request):

        # 4. Model을 활용하여 Database에서 계정 정보를 받아와서 처리하기
        userid = request.POST['userid']
        userpw = request.POST['userpw']
        # DB에서 userid를 기준으로 계정을 가져와서
        # 해당 계정의 dbpw와 userpw가 일치하면 context에 계정으로 담아서 전달
        context = {
            'result' : '로그인 실패'
        }
        q = models.Login.objects.all().filter(userid__contains = userid)
        for member in q:
            if member.userpw == userpw:
                context['result'] = '{} 님 환영합니다'.format(member.username)
                break
        return render(request, 'app1/login_result.html', context)