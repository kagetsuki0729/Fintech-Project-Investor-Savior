from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home.html')

from graphos.sources.simple import SimpleDataSource
from graphos.renderers.gchart import LineChart
import csv
with open("savior/test.csv") as file:
    reader=csv.reader(file)
    data=list(reader)
for i in range(1,len(data)):
    for j in range(1,len(data[i])):
        data[i][j]=int(data[i][j])
print(data)
'''data = [
       ['Year', 'Sales', 'Expenses', 'Items Sold', 'Net Profit'],
       ['2004', 1000, 400, 100, 600],
       ['2005', 1170, 460, 120, 710],
       ['2006', 660, 1120, 50, -460],
       ['2007', 1030, 540, 100, 490],
       ]
'''
# DataSource object
data_source = SimpleDataSource(data=data)
# Chart object
chart = LineChart(data_source)
context = {'chart': chart}
def diagram(request):
    return render(request, 'diagram.html',context)
