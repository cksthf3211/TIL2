# 프로젝트 생성

## 생성

1. 프로젝트 폴더 생성
2. conda 가상환경 만들기 (Anaconda navigator)
3. conda list
4. pip list

5. 가상환성 활성화 (activate 가상환경이름) or (deactivate) or (conda env remove -n 가상환경이름)
6. conda list
7. pip list

8. python 생성
9. pip install django (django 생성)
10. pip install djangorestframework (django 확장)
11. pip install mysqlclient (MySQL연동)

12. django-admin startproject 프로젝트이름
13. python manage.py startapp 앱이름
14. python manage.py inspectdb (db table 자동 생성 - 복사해서 models.py에 업데이트)
15. python manage.py runserver

## Setting

### settings.py

- from my_settings import mySECRET_KEY, myDATABASES

- INSTALLED_APPS = [ 앱등록 ]

- SECRET_KEY = mySECRET_KEY (SECRET_KEY는 my_settings.py에 분리)
- DATABASES = myDATABASES
- Allowed_hosts = ["*"]
- LANGUAGE_CODE = 'ko-kr'
- TIME_ZONE = 'asia/seoul'

### my_settings.py

_manage.py와 동일한 위치에 생성_

- mySECRET_KEY = '[SECRET_KEY]'

myDATABASES = {
'default' : {
'ENGINE' : 'django.db.backends.mysql', (벡엔드 엔진)
'NAME' : 'ADR_DB', ('mysql'의 이름을 가진 데이터베이스 이름)
'USER' : 'root', (계정)
'PASSWORD' : '비번',(rootpassword로 지정할 숫자(6번에 나와있음))
'HOST' : '127.0.0.1',
'PORT' : '3306'
}
}
