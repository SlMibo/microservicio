from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import User
import json
# Create your views here.

class UserView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id>0):
            users = list(User.objects.filter(id=id).values())
            if len(users) > 0:
                user = users[0]
                datos = {'message':'Success', 'users': user}
            else:
                datos = {'message':'No se encuentra el usuario...'}
            return JsonResponse(datos)
        else:
            users = list(User.objects.values())
            if len(users) > 0:
                datos = {'message':'Success', 'users': users}
            else:
                datos = {'message':'No hay usuarios...'}
            return JsonResponse(datos)

    def post(self, request):
        
        jd = json.loads(request.body)

        User.objects.create(name=jd['name'], surname=jd['surname'], email=jd['email'], password=jd['password'])
        datos = {'message':'Success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            user = User.objects.get(id=id)
            user.name=jd['name']
            user.surname=jd['surname']
            user.email=jd['email']
            user.password=jd['password']
            user.save()
            datos = {'message':'Success'}
        else:
            datos = {'message':'No se encuentra el usuario...'}
        return JsonResponse(datos)

    def delete(self, request, id):
        users = list(User.objects.filter(id=id).values())
        if len(users) > 0:
            User.objects.filter(id=id).delete()
            datos = {'message':'Success'}
        else:
            datos = {'message':'No se encuentra el usuario...'}
        return JsonResponse(datos)