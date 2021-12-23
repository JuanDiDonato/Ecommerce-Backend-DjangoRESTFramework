# Rest framework
from rest_framework import viewsets, status
from rest_framework.response import Response

# Authentication
from apps.users.authenticate import RoleAuthentication
"""
Authentication for tokens in headers
"""
# from rest_framework.permissions import IsAuthenticated

# Serializers
from apps.products.api.serializers import (ColorsSerializer, ProductSerializer, 
    EventSerializer, CategorySerializer, 
    WaistSerializer, ImageSerializer)

# Categories
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (RoleAuthentication,)
    
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
    permission_classes = (RoleAuthentication,)

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
    permission_classes = (RoleAuthentication,)
    
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
    permission_classes = (RoleAuthentication,)
    queryset = ColorsSerializer.Meta.model.objects.all()

# Waist
class WaistViewSet(viewsets.ModelViewSet):
    serializer_class = WaistSerializer
    queryset = WaistSerializer.Meta.model.objects.all()
    permission_classes = (RoleAuthentication,)

# Images
class ImagesViewSet(viewsets.GenericViewSet):
    serializer_class = ImageSerializer
    permission_classes = (RoleAuthentication,)

    def get_queryset(self, pk=None):
        if pk:
            return self.get_serializer().Meta.model.objects.filter(product=pk)
        else:
            return self.get_serializer().Meta.model.objects.all()


    def list(self, request):
        product = None
        if request.GET:
            product = request.GET['product']

        if product:
            image_serializer = self.get_serializer(self.get_queryset(product),many=True)
        else:
            image_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(image_serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Foto agregada!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        image = self.get_queryset().filter(id=pk).first() # get instance        
        if image:
            image.delete()
            return Response({'message':'Operacion completada.'},status=status.HTTP_200_OK)
        return Response({'error':'La imagen no existe.'},status=status.HTTP_400_BAD_REQUEST)