from django.urls import path
from loginregisterlogout.views import *

urlpatterns = [
    path('employee/create/', EmployeeCreateAPIView.as_view(), name='employeecreate'),
    path('employee/update/<pk>/',
         EmployeeUpdateAPIView.as_view(), name='employeeupdate'),
    path('employeelist/', EmployeeListAPIView.as_view(), name='employeelist'),
    path('employeedelete/<pk>/',
         EmployeeDestroyAPIView.as_view(), name='employeedelete'),
    path('employee/retrieve/<pk>/',
         EmployeeRetrieveAPIView.as_view(), name='employeeretrieve')
]
