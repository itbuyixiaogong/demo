import json

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

from django.views.decorators.csrf import csrf_exempt
from students.models import Stu
import MySQLdb
@csrf_exempt  
def demo(request):
    ret = {1: "hello", 2: "demo"}
    # db = MySQLdb.connect(user='root', db='demo', passwd='', host='')
    # cursor = db.cursor()
    # cursor.execute('SELECT id,name,score FROM stu')
    # # names = [row[0] for row in cursor.fetchall()]
    # # print(names) 
    # stu=cursor.fetchall()
    # print(stu)
    # db.close()
   
    if 'name' in request.GET and request.GET['name']:
        name = request.GET['name']
        stu=Stu.objects.filter(name__icontains=name)
        # print(stu)
        for s in stu:
            print(s.stuid+","+s.name+","+s.score)
            str={'stuid':s.stuid,'name':s.name,'score':s.score}
            return HttpResponse(json.dumps(str))
    # else:
    #     print("empty")
    # return HttpResponse(json.dumps(ret))
    
    # stu=Stu.objects.all()
    # print(stu)
    # return render_to_response('list.html',{'stu':stu})
    
    elif request.method=='POST':
        stuid=request.POST.get('stuid')
        name=request.POST.get('name')
        score=request.POST.get('score')
        stu1=Stu(stuid=stuid,name=name,score=score)
        stu1.save()
        return HttpResponse(json.dumps(ret))
    return HttpResponse(json.dumps(ret))


# from django.http import Http404, HttpResponseRedirect
# from django.shortcuts import render_to_response

# def method_splitter(request, GET=None, POST=None):
#     if request.method == 'GET' and GET is not None:
#         return GET(request)
#     elif request.method == 'POST' and POST is not None:
#         return POST(request)
#     raise Http404
# def some_page_get(request):
#     assert request.method == 'GET'
#     print("this is get")
#     # do_something_for_get()
#     return render_to_response('index.html')

# def some_page_post(request):
#     assert request.method == 'POST'
#     print("this is post")
#     # do_something_for_post()
#     return HttpResponseRedirect('/demo/')