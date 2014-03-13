from django.db import models

# Create your models here.
class Sample(models.Model):
    delegationNum= models.CharField(max_length=30)
    delegationUnit = models.CharField(max_length=30)
    delegationName = models.CharField(max_length=30)
    delegationTime = models.CharField(max_length=30)
    delegationUnitAddr = models.CharField(max_length=30)
    delegationZipCode = models.CharField(max_length=30)
    delegationTel = models.CharField(max_length=30)
    delegationFax = models.CharField(max_length=30)
    delegationAccount = models.CharField(max_length=30)
    delegationAccountBank = models.CharField(max_length=30)
    delegationAccountBankAddr = models.CharField(max_length=30)
    projectPersonInCharge = models.CharField(max_length=30)
    entrustedTime = models.CharField(max_length=30)

    sampleNum = models.CharField(max_length=30)
    sampleMaterial = models.CharField(max_length=30)
    sampleSize = models.CharField(max_length=30)
    sampleData = models.CharField(max_length=30)
    sampleGrade = models.CharField(max_length=30)
    sampleStandard = models.CharField(max_length=30)

    storageLocation = models.CharField(max_length=30)
    storagePersoInCharge = models.CharField(max_length=30)
    
    def __unicode__(self):
    	return self.delegationNum

class SamplePreProcessing(models.Model):
    sendSamplePersonInCharge= models.CharField(max_length=30)
    sendSampleTime= models.CharField(max_length=30)
    predictPreProcessingTime= models.CharField(max_length=30)

    storageLocation= models.CharField(max_length=30)
    storagePersonInCharge= models.CharField(max_length=30)

    receivePersonInCharge= models.CharField(max_length=30)
    receiveTime= models.CharField(max_length=30)

    def __unicode__(self):
        return self.sendSamplePersonInCharge

class SampleExperiment(models.Model):
    predictExperimentItem= models.CharField(max_length=30)
    experimentType= models.CharField(max_length=30)
    experimentPersonInCharge= models.CharField(max_length=30)
    experimentLocation= models.CharField(max_length=30)
    testingStandard= models.CharField(max_length=30)
    predictExperimentStartTime= models.CharField(max_length=30)
    predictExperimentFinishTime= models.CharField(max_length=30)

    abnormalReasons= models.CharField(max_length=30)
    abnormalTime= models.CharField(max_length=30)
    remark= models.CharField(max_length=30)

    resultDescribe= models.CharField(max_length=30)
    resultImg= models.CharField(max_length=30)
    resultReport= models.CharField(max_length=30)

    def __unicode__(self):
        return self.predictExperimentItem