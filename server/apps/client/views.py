# Rest framework
from rest_framework import viewsets, status
from rest_framework.response import Response

#Serializers
from apps.client.api.serializers import ShoppingCartSerializer, ShoppingHistorySerializer

# View with ViewSets
class ShoppingCartViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppingCartSerializer

    def get_queryset(self, pk=None):
        if pk:
            return self.get_serializer().Meta.model.objects.filter(user=pk)
        else:
            return self.get_serializer().Meta.model.objects.all()


    def list(self, request):
        """
        Lista los objetos del carrito.
        """
        user = None
        if request.GET:
            user = request.GET['user']

        if user:
            shopping_cart_serializer = self.get_serializer(self.get_queryset(user),many=True)
        else:
            shopping_cart_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(shopping_cart_serializer.data,status=status.HTTP_200_OK)

    def create(self, request):
        """
        Agrega un producto al carrito.
        """
        serializer = self.serializer_class(data=request.data)     
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Producto agregado al carrito!'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        """
        Actualiza una instancia del carrito.
        """
        if self.get_queryset(pk):
            # send information to serializer referencing the instance
            shopping_cart_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)            
            if shopping_cart_serializer.is_valid():
                shopping_cart_serializer.save()
                return Response(shopping_cart_serializer.data,status=status.HTTP_200_OK)
            return Response(shopping_cart_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None):
        """
        Borra una instancia del carrito.
        """
        cart = self.get_queryset().filter(id_cart=pk).first() # get instance        
        if cart:
            cart.delete()
            return Response({'message':'Producto removido con exito.'},status=status.HTTP_200_OK)
        return Response({'error':'El producto no esta en el carrito.'},status=status.HTTP_400_BAD_REQUEST)

class ShoppingHistoryViewSet(viewsets.GenericViewSet):
    serializer_class = ShoppingHistorySerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id_history=pk).first()

    def list(self,request):
        """
        Retorna el historial de compras.
        """
        shopping_history_serializer = self.get_serializer(self.get_queryset(),many=True)
        return Response(shopping_history_serializer.data,status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """
        Permite obtener una instancia especifica.
        """
        history = self.get_queryset(pk)
        shopping_history_serializer = self.serializer_class(history)
        return Response(shopping_history_serializer.data,status=status.HTTP_200_OK)

    def create(self,request):
        """
        Crea un nuevo registro en el historial.
        """
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Compra agregada al historial.'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        """
        Actualiza el historial, para cambiar el estado.
        """
        history_data = self.get_queryset(pk)
        if history_data:
            shopping_history_serializer = self.serializer_class(history_data,request.data)
            if shopping_history_serializer.is_valid():
                shopping_history_serializer.save()
                return Response({'message':'Estado actualizado.'},status=status.HTTP_200_OK)
            return Response(shopping_history_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


