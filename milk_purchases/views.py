from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import MilkPurchase
from .serializers import serializerCompraLeite


class CompraLeiteViewSet(ModelViewSet):
    queryset = MilkPurchase.objects.all()
    serializer_class = serializerCompraLeite
    permission_classes = [IsAuthenticated]