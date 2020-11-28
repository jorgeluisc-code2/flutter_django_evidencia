from django.http import Http404, request
from django.shortcuts import render
from rest_framework import generics, filters, status
from search.models import Category, Employee, categoria
from search.serializers import FoodSerializer, EmployeeSerializer, categoriaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class FoodAPIView(generics.ListCreateAPIView):
    search_fields = ['id', 'name']
    filter_backends = (filters.SearchFilter,)
    queryset = Category.objects.all()
    serializer_class = FoodSerializer




class categoraTable(APIView):

    def get(self, request):
        categoriaobj = categoria.objects.all()
        categoriaseriobj = categoriaSerializer(categoriaobj, many=True)
        return Response(categoriaseriobj.data)


class SnippetList(APIView):
    search_fields = ['id', 'name']
    filter_backends = (filters.SearchFilter,)
    queryset = Category.objects.all()
    serializer_class = FoodSerializer

    def get(self, request, format=None):
        snippets = Category.objects.all()
        serializer = FoodSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def save(self, request, nombre, format=None):
        objeto = Category(name=nombre)
        objeto.save()

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class SnippetDetail(APIView):
    queryset = Category.objects.all()
    serializer_class = FoodSerializer

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FoodSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = FoodSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def elimimnarCategoria(request,pk):
    categoria = Category.objects.get(name=pk)
    categoria.delete()


def Crear(request, name):
    categoria = name
    objeto = Category(name=categoria)
    objeto.save()
    return render(request, 'index.html')