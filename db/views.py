from django.http.response import JsonResponse
from django.views import View
from django.shortcuts import render
from mongo.models import PersonMongo
from postgresql.models import PersonPostgresql
import time



class TestIndex(View):
    def __init__(self):
        self.mongoAll = PersonMongo.objects.all()
        self.postgreall = PersonPostgresql.objects.all()
    def get(self,request):  
        return render(request,'test.html',{'mongo':self.mongoAll,'postgre':self.postgreall})

    def post(self,request):
        try:
            if request.POST.dict()['type'] == "mongo":
                print("mongo----->",request.POST.dict())
                start = time.time()
                mongo = PersonMongo(name=request.POST.dict()['name'],surname=request.POST.dict()['surname'],school=request.POST.dict()['school'],year=request.POST.dict()['year'])
                mongo.save()
                stop = time.time()
                #print((stop-start)*1000.0)
                return JsonResponse({'time':(stop-start)*1000.0})
            elif request.POST.dict()['type'] == "postgresql":
                print("postgre----->",request.POST.dict())
                start = time.time()
                postgre = PersonPostgresql(name=request.POST.dict()['name'],surname=request.POST.dict()['surname'],school=request.POST.dict()['school'],year=request.POST.dict()['year'])
                postgre.save()
                stop = time.time()
                #print((stop-start)*1000.0)
                return JsonResponse({'time':(stop-start)*1000.0})
        except Exception as err:
            return JsonResponse({'time':'{}'.format(err)})
    

def delete(request):
    print("--------------")
    try:
        if request.POST.dict()['type'] == 'mongo':
            start = time.time()
            PersonMongo.objects.filter(id=request.POST.dict()['value']).delete()
            stop = time.time()
            return JsonResponse({'time':(stop-start)*1000.0})
        elif request.POST.dict()['type'] == 'postgesql':
            start = time.time()
            PersonPostgresql.objects.filter(id=request.POST.dict()['value']).delete()
            stop = time.time()
            return JsonResponse({'time':(stop-start)*1000.0})
        else:
            return JsonResponse({'time':'HATA'})
    except Exception as err:
            return JsonResponse({'time':'{}'.format(err)})
    