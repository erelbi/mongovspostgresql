from django.db import models


class PersonPostgresql(models.Model):
    name = models.CharField(max_length=20,null=True)
    surname = models.CharField(max_length=20,null=True)
    year = models.IntegerField()
    school =  models.CharField(max_length=20,null=True)
    # class Meta:
    #     app_label = 'postresql'

# Create your models here.
