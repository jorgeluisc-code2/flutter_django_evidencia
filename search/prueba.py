from django.http import Http404
from django.shortcuts import render
from rest_framework import generics, filters, status
from search.models import Category, Employee, categoria
from search.serializers import FoodSerializer, EmployeeSerializer,categoriaSerializer
from search.models import Food, Category

#def guardar(self, request, nombre, format=None):

#    objeto=Category(name=nombre)
#    objeto.save()


#objeto=Employee(emplyee_regNo="3",emplyee_name="jorge",employee_email="jorge@gmail.com",employee_mobile="987654321",created_at="10/10/10")

#objeto.save()



