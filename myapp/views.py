from django.shortcuts import render

# from django.http import HttpResponse
import pandas as pd
from pandas.io import json

from .models import Data

# Create your views here.

def hello(request):

    # return HttpResponse("<h1>Hello there</h1>")

    # name='BOB'
    # price=100
    # movies=['Superman','Spiderman','Batman']

    # context={'movies':movies}

    # print(request.method)

    if(request.method=='POST'):

        print("This is a post request")

        previous_data=Data.objects.all()
        previous_data.delete()

        # name=request.POST.get("name")
        # print(name) # We are printing the name variable which contains the "name"

        # print(request.FILES['file'])

        file=request.FILES['file']
        # print(pd.read_csv(file))

        df=pd.read_csv(file)
        json_records=df.reset_index().to_json(orient='records')
        data=[]
        data=json.loads(json_records)

        for i in data:
            property_name=i['property_name']
            property_price=i['property_price']
            property_rent=i['property_rent']
            emi=i['emi']
            tax=i['tax']
            other_exp=i['other_exp']

            monthly_expenses=emi+tax+other_exp
            monthly_income=property_rent-monthly_expenses
  

            dt=Data(property_name=property_name, property_price=property_price, property_rent=property_rent, emi=emi, tax=tax, 
                    other_exp=other_exp, monthly_expenses=monthly_expenses, monthly_income=monthly_income)

            dt.save()

        data_objects=Data.objects.all()
        context={'data_objects':data_objects}

        return render(request,"myapp/index.html",context)

        # print(data)
        # print(json_records)

    else:

        print("This is a get request")

    return render(request,"myapp/index.html")

