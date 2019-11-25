from django.db import models

# Create your models here.

# 1. 테이블을 파이썬 클래스로 정의한다(admin.py 등록, register)
class Login(models.Model):
    userid = models.CharField(max_length=20)
    userpw = models.CharField(max_length=20)
    username = models.CharField(max_length=10)

# 2. DB파일에 저장할 내용을 django에 전달하기 위해서
# py manage.py makemigraions
# 3. 전달받은 내용을 DB파일에 적용하기 위해서
# py manage.py migrate
# 4. admin 페이지에서 Logins 테이블에 Login 객체를 생성한다