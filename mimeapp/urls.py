from django.contrib import admin
from django.urls import path
from .views import Htmlview,Xmlview,Excelview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('html',Htmlview.as_view()),
    path('xml',Xmlview.as_view()),
    path('excel',Excelview.as_view()),

]