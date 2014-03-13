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
   
    ret = {1: "hello", 2: "demo"}
    if 'name' in request.GET and request.GET['name']:
        name = request.GET['name']
        stu=Stu.objects.filter(name__icontains=name)
        # print(stu)
        for s in stu:
            print(s.stuid+","+s.name+","+s.score)
            str={'stuid':s.stuid,'name':s.name,'score':s.score}
            return HttpResponse(json.dumps(str))
    elif request.method=='POST':
        stuid=request.POST.get('stuid')
        name=request.POST.get('name')
        score=request.POST.get('score')
        stu1=Stu(stuid=stuid,name=name,score=score)
        stu1.save()
        # return HttpResponse(json.dumps(ret))
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

from samples.models import Sample
@csrf_exempt
def receptionAndStorage(request):
    if request.method=='POST':
        delegationNum=request.POST.get('delegationNum')
        delegationUnit=request.POST.get('delegationUnit')
        delegationName=request.POST.get('delegationName')
        delegationTime=request.POST.get('delegationTime')
        delegationUnitAddr=request.POST.get('delegationUnitAddr')
        delegationZipCode=request.POST.get('delegationZipCode')
        delegationTel=request.POST.get('delegationTel')
        delegationFax=request.POST.get('delegationFax')
        delegationAccount=request.POST.get('delegationAccount')
        delegationAccountBank=request.POST.get('delegationAccountBank')
        delegationAccountBankAddr=request.POST.get('delegationAccountBankAddr')
        projectPersonInCharge=request.POST.get('projectPersonInCharge')
        entrustedTime=request.POST.get('entrustedTime')

        sampleNum=request.POST.get('sampleNum')
        sampleMaterial=request.POST.get('sampleMaterial')
        sampleSize=request.POST.get('sampleSize')
        sampleData=request.POST.get('sampleData')
        sampleGrade=request.POST.get('sampleGrade')
        sampleStandard=request.POST.get('sampleStandard')

        storageLocation=request.POST.get('storageLocation')
        storagePersoInCharge=request.POST.get('storagePersoInCharge')

        s1=Sample(delegationNum=delegationNum,delegationUnit=delegationUnit,delegationName=delegationName,
            delegationTime=delegationTime,delegationUnitAddr=delegationUnitAddr,delegationZipCode=delegationZipCode,
            delegationTel=delegationTel,delegationFax=delegationFax,delegationAccount=delegationAccount,
            delegationAccountBankAddr=delegationAccountBankAddr,projectPersonInCharge=projectPersonInCharge,entrustedTime=entrustedTime, 
            sampleNum=sampleNum,sampleMaterial=sampleMaterial,sampleData=sampleData,sampleGrade=sampleGrade,sampleStandard=sampleStandard,
            storageLocation=storageLocation,storagePersoInCharge=storagePersoInCharge)
        s1.save()
        status='success'
    else:
        status='error'
    return HttpResponse(json.dumps(status))

from samples.models import SamplePreProcessing
@csrf_exempt
def samplePreProcessing(request):
    if request.method=='POST':
        sendSamplePersonInCharge=request.POST.get('sendSamplePersonInCharge')
        sendSampleTime=request.POST.get('sendSampleTime')
        predictPreProcessingTime=request.POST.get('predictPreProcessingTime')

        storageLocation=request.POST.get('storageLocation')
        storagePersonInCharge=request.POST.get('storagePersonInCharge')

        receivePersonInCharge=request.POST.get('receivePersonInCharge')
        receiveTime=request.POST.get('receiveTime')
        s1=SamplePreProcessing(sendSamplePersonInCharge=sendSamplePersonInCharge,sendSampleTime=sendSampleTime,
            predictPreProcessingTime=predictPreProcessingTime,storageLocation=storageLocation,storagePersonInCharge=storagePersonInCharge,
            receivePersonInCharge=receivePersonInCharge,receiveTime=receiveTime)
        s1.save()
        status='success'
    else:
        status='error'
    return HttpResponse(json.dumps(status))

from samples.models import SampleExperiment
@csrf_exempt
def sampleExperiment(request):
    if request.method=='POST':
        predictExperimentItem=request.POST.get('predictExperimentItem')
        experimentType=request.POST.get('experimentType')
        experimentPersonInCharge=request.POST.get('experimentPersonInCharge')
        experimentLocation=request.POST.get('experimentLocation')
        testingStandard=request.POST.get('testingStandard')
        predictExperimentStartTime=request.POST.get('predictExperimentStartTime')
        predictExperimentFinishTime=request.POST.get('predictExperimentFinishTime')

        abnormalReasons=request.POST.get('abnormalReasons')
        abnormalTime=request.POST.get('abnormalTime')
        remark=request.POST.get('remark')

        resultDescribe=request.POST.get('resultDescribe')
        resultImg=request.POST.get('resultImg')
        resultReport=request.POST.get('resultReport')

        s1=SampleExperiment(predictExperimentItem=predictExperimentItem,experimentType=experimentType,
            experimentPersonInCharge=experimentPersonInCharge,experimentLocation=experimentLocation,
            testingStandard=testingStandard,predictExperimentStartTime=predictExperimentStartTime,
            predictExperimentFinishTime=predictExperimentFinishTime,abnormalReasons=abnormalReasons,
            abnormalTime=abnormalTime,remark=remark,resultDescribe=resultDescribe,resultImg=resultImg,
            resultReport=resultReport)
        s1.save()
        status='success'
    else:
        status='error'
    return HttpResponse(json.dumps(status))