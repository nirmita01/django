from .serializers import CustomerSerializer
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from customer.models import Customer
from rest_framework.permissions import IsAuthenticated


class CustomerListView(GenericAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all() 
    permission_classes = [IsAuthenticated]

    def get(self, request):
        customers = self.get_queryset()
        serializer = self.get_serializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CustomerDetailsAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field = "customer_id"