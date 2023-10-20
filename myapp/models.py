from django.db import models

# Create your models here.

class Data(models.Model):

    property_name=models.CharField(max_length=200)
    property_price=models.IntegerField()
    property_rent=models.IntegerField()
    emi=models.IntegerField()
    tax=models.IntegerField()
    other_exp=models.IntegerField()
    monthly_expenses=models.IntegerField(default=0)
    monthly_income=models.IntegerField(default=0)
    


