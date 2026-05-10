from rest_framework.serializers import ModelSerializer
from .models import MilkPurchase


class serializerCompraLeite(ModelSerializer):
    class Meta:
        model = MilkPurchase
        fields = '__all__'