from django.db import models

class PersonMongo(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    year = models.IntegerField()
    school =  models.CharField(max_length=20)
    # class Meta:
    #     app_label = 'mongo'
