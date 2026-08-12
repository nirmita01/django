from .serializers import SupplierSerializer
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from suppliers.models import Supplier

class SupplierListView(GenericAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()

    def get(self, request):
        suppliers = self.get_queryset()
        serializer = self.get_serializer(suppliers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class SupplierDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.all()
    lookup_field = "supplier_id"