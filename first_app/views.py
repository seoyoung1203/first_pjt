import random
from faker import Faker
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    my_name = 'seoyoung'

    context = {
        'my_name': my_name,
    }

    return render(request, 'hello.html', context)

def lunch(request):
    menu = ['김밥', '초밥', '돈까스', '우동']
    
    pick = random.choice(menu)

    context = {
        'pick': pick,
    }

    return render(request, 'lunch.html', context)

def lotto(request):
    lucky_number = random.sample(range(1, 46), 6)

    # number = random.choice(lucky_number)

    context = {
        'lucky_number': lucky_number,
    }


    return render(request, 'lotto.html', context)


def profile(request, username):
    context = {
        'asdf': username,
    }

    return render(request, 'profile.html', context)

def cube(request, number):
    result = number ** 3

    context = {
        'number': number,
        'result': result,
    }

    return render(request, 'cube.html', context)

def articles(request):
    fake = Faker()
    fake_articles = []

    for i in range(100):
        fake_articles.append(fake.text())

    context = {
        'fake_articles': fake_articles,
    }

    return render(request, 'articles.html', context)

    # def news(request, ):
    #     top_news = 
