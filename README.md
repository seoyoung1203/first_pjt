# gitignore 


# 가상환경 설정


## 1. Django  프로젝트


1. Django 설치
```shell
pip install django
```

2. 프로젝트 생성
```
django-admin startproject <pjt-name> <path>
```

3. 서버 실행
서버 종료 >> ctrl + c
```
python manage.py runserver

4. 앱 생성
```shell
django-admin startapp <app.name>
```

5. 앱 등록('settings.py')
```python
INSTALLED_APPS = [

]
```

MTV(templates, models, views)
client > urls.py(어떤 경로로 받을지 -> path) > Views.py(실행시키고 싶은 함수 함수 이름은 경로와 맞추기. 선언과 불러오는 것은 각각) > models.py > template(HTML) 데이터 수정 > view.py >> (사이클 반복) >>> (최종) response(HTML)


{% for fake_article in fake_articles %}
        <p>{{fake_article}}</p>
    {% endfor %}
    >> 잔고에서 파이썬 코드 활용법

    . >> class + tab (div 활용)
    # >> id 
