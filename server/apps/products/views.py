from rest_framework import viewsets, status
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticated

# Serializers
from apps.products.api.serializers import ColorsSerializer, ProductSerializer, EventSerializer, CategorySerializer, WaistSerializer

# Categories
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    
    def get_queryset(self,pk=None):
        if not pk:
            return self.get_serializer().Meta.model.objects.all()
        else :
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()
    
    # I edit the update method for change the response.
    def update(self,request,pk=None,*args,**kwargs):
        category = self.get_queryset(pk)
        if category:
            category_serializer = self.get_serializer(category,data=request.data)
            if category_serializer.is_valid():
                category_serializer.save()
                return Response({'message':'Categoria actualizada'},status=status.HTTP_200_OK)
        return Response({'message':'Categoria no encontrada.'},status=status.HTTP_400_BAD_REQUEST)

# Events
class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    
    def get_queryset(self,pk=None):
        if not pk:
            return self.get_serializer().Meta.model.objects.all()
        else :
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def update(self,request,pk=None,*args,**kwargs):
        event = self.get_queryset(pk)
        if event:
            event_serializer = self.get_serializer(event,data=request.data)
            if event_serializer.is_valid():
                event_serializer.save()
                return Response({'message':'Evento actualizado'},status=status.HTTP_200_OK)
        return Response({'message':'Evento no encontrado.'},status=status.HTTP_400_BAD_REQUEST)

# Products
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    # permission_classes = (IsAuthenticated,) # Para que requiera el token la mostrar los datos
    
    def get_queryset(self,pk=None):
        if not pk :
            return self.get_serializer().Meta.model.objects.all()
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response({'error':True, 'message':serializer.errors },status=status.HTTP_400_BAD_REQUEST)

    # I edit the update method for change the response.
    def update(self,request,pk=None,*args,**kwargs):
        product = self.get_queryset(pk)
        if product:
            product_serializer = self.get_serializer(product,data=request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response({'message':'Producto actualizado.'},status=status.HTTP_200_OK)
        return Response({'message':'Producto no encontrado.'},status=status.HTTP_400_BAD_REQUEST)

# Colors
class ColorViewSet(viewsets.ModelViewSet):
    serializer_class = ColorsSerializer
    queryset = ColorsSerializer.Meta.model.objects.all()

# Waist
class WaistViewSet(viewsets.ModelViewSet):
    serializer_class = WaistSerializer
    queryset = WaistSerializer.Meta.model.objects.all()

"""
# Waist and colors
class WaistAndColorViewSet(viewsets.ModelViewSet):
    serializer_class = WaistAndColorSerializer
    
    def get_queryset(self,pk=None):
        if not pk:
            return self.get_serializer().Meta.model.objects.all()
        else :
            return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error':False},status=status.HTTP_201_CREATED)
        return Response({'error':True, 'message':serializer.errors },status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None,*args,**kwargs):
        waist_and_color = self.get_queryset(pk)
        if waist_and_color:
            waist_and_color_serializer = self.get_serializer(waist_and_color,data=request.data)
            if waist_and_color_serializer.is_valid():
                waist_and_color_serializer.save()
                return Response({'message':'Color y talles actualizados.'},status=status.HTTP_200_OK)
        return Response({'message':'Datos no encontrados.'},status=status.HTTP_400_BAD_REQUEST)
"""



