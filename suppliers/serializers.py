from rest_framework.serializers import ModelSerializer
from .models import Fornecedor


class FornecedorSerializer(ModelSerializer):
    class Meta:
        model = Fornecedor
        fields = '__all__'