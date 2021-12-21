# Rest framework
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

# Authentication
from apps.users.authenticate import RoleAuthentication

# Serializers
from apps.mod.api.serializers import StatisticSerializer, MonthlyStatisticSerializer, PendingShipmentsSerializer

# Pending shipments
class PendingShipmentsViewSet(viewsets.ModelViewSet):
    serializer_class = PendingShipmentsSerializer
    permission_classes = (RoleAuthentication,)
    queryset = PendingShipmentsSerializer.Meta.model.objects.all()

# Statistics
class StatisticViewSet(viewsets.GenericViewSet):
    serializer_class = StatisticSerializer
    permission_classes = (RoleAuthentication,)
        
    def get_queryset(self,pk=None):
        return self.get_serializer().Meta.model.objects.all()

    
    def list(self,request):
        statistics = self.get_queryset()
        statistics = self.get_serializer(statistics,many=True)
        return Response(statistics.data,status=status.HTTP_200_OK)

    # Add new statistics
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error':False},status=status.HTTP_201_CREATED)
        return Response({'error':True, 'message':serializer.errors },status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk=None,*args,**kwargs):
        statistic = self.get_queryset()
        if statistic:
            statistic.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({'message':'No hay estadisticas'},status=status.HTTP_400_BAD_REQUEST)

# Monthly statistics
class MonthlyStatisticViewSet(viewsets.GenericViewSet):
    serializer_class = MonthlyStatisticSerializer
    permission_classes = (RoleAuthentication,)

    def get_queryset(self,pk=None):
        return self.get_serializer().Meta.model.objects.all()

    def list(self,request):
        statistics = self.get_queryset()
        statistics = self.get_serializer(statistics,many=True)
        return Response(statistics.data,status=status.HTTP_200_OK)

    # Add new statistics
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'error':False},status=status.HTTP_201_CREATED)
        return Response({'error':True, 'message':serializer.errors },status=status.HTTP_400_BAD_REQUEST)