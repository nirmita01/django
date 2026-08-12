from rest_framework import serializers
from suppliers.models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ["name", "email", "phone", "address"]
        read_only_fields = ["supplier_id"]
