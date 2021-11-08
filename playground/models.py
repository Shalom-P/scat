from django.db import models

# Create your models here. 

class Newcat(models.Model):
    sentence = models.CharField('Sentence',max_length=200)
    label = models.CharField('Label',max_length=1)

    def __str__(self):
        return self.sentence

class Newslearnwion(models.Model):
    sent = models.CharField('sentence',max_length=300,primary_key=True)
    title1 = models.CharField('title1',max_length=200)
    link1 = models.CharField('link1',max_length=500,null=True)
    title2 = models.CharField('title2',max_length=200)
    link2 = models.CharField('link2',max_length=500,null=True)
    title3 = models.CharField('title3',max_length=200)
    link3 = models.CharField('link3',max_length=500,null=True)
    title4 = models.CharField('title4',max_length=200,null=True)
    link4 = models.CharField('link4',max_length=500,null=True)
    title5 = models.CharField('title5',max_length=200,null=True)
    link5 = models.CharField('link5',max_length=500,null=True)
    def __str__(self):
        return self.sent

class Newslearnbbc(models.Model):
    sent = models.CharField('sentence',max_length=300,primary_key=True)
    title1 = models.CharField('title1',max_length=200)
    link1 = models.CharField('link1',max_length=500,null=True)
    title2 = models.CharField('title2',max_length=200)
    link2 = models.CharField('link2',max_length=500,null=True)
    title3 = models.CharField('title3',max_length=200)
    link3 = models.CharField('link3',max_length=500,null=True)
    title4 = models.CharField('title4',max_length=200,null=True)
    link4 = models.CharField('link4',max_length=500,null=True)
    title5 = models.CharField('title5',max_length=200,null=True)
    link5 = models.CharField('link5',max_length=500,null=True)
    def __str__(self):
        return self.sent

class Newslearneuronews(models.Model):
    sent = models.CharField('sentence',max_length=300,primary_key=True)
    title1 = models.CharField('title1',max_length=200)
    link1 = models.CharField('link1',max_length=500,null=True)
    title2 = models.CharField('title2',max_length=200)
    link2 = models.CharField('link2',max_length=500,null=True)
    title3 = models.CharField('title3',max_length=200)
    link3 = models.CharField('link3',max_length=500,null=True)
    title4 = models.CharField('title4',max_length=200,null=True)
    link4 = models.CharField('link4',max_length=500,null=True)
    title5 = models.CharField('title5',max_length=200,null=True)
    link5 = models.CharField('link5',max_length=500,null=True)
    def __str__(self):
        return self.sent