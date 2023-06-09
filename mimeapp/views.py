from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
data="""<table>
  <tr>
    <th>Month</th>
    <th>Savings</th>
  </tr>
  <tr>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>"""
class Htmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/h")
class Xmlview(View):
    def get(self,request):
        return HttpResponse(data,content_type="applicalation/xml")
class Excelview(View):
    def get(selfself):
        return HttpResponse(data,content_type="application/vnd.ms-excel")

