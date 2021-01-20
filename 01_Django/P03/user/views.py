import redis
from django.http import HttpResponse
from django.shortcuts import render
from .models import User

# Create your views here.
r = redis.Redis(host="localhost", port=6379, decode_responses=True)


def user_detail(request, uid):
    # return HttpResponse('user_detail')
    cache_key = 'user_%s' % uid
    if r.exists(cache_key):
        data = r.hgetall(cache_key)
        # {'name': 'aid2010', 'age': '18', 'city': '北京'}
        print(data)
        username = data['username']
        age = data['age']
        result = 'cache:username is %s,age is %s' % (username, age)
        return HttpResponse(result)

    else:
        try:
            user = User.objects.get(id=uid)
        except:
            return HttpResponse('user not alive')
        r.hmset(cache_key, {'username': user.username, 'age': user.age})
        r.expire(cache_key, 60)
        result = 'mysql:username is %s,age is %s' % (user.username, user.age)
        return HttpResponse(result)


def user_update(request,uid):
    age = request.GET.get('age',20)
    try:
        user = User.objects.get(id=uid)
    except :
        return HttpResponse('Id mistake')
    user.age = age
    user.save()
    cache_key = 'user_%s' % uid
    r.delete(cache_key)




    return HttpResponse('Update age success!')


