from rest_framework import viewsets
from API.models.loyalityModel import Loyalty
from API.serializers.loyaltySerializer import LoyaltySerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


class LoyaltyViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Loyalty.objects.all()
    serializer_class = LoyaltySerializer
    def get_Loyality(self, loyality_id):
        try:
            return Loyalty.objects.get(id=loyality_id)
        except Loyalty.DoesNotExist:
            return None

    def get(self, request, loyality_id, *args, **kwargs):
        loyality = self.get_Loyality(loyality_id)
        if not loyality:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = LoyaltySerializer(loyality)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        loyality = {
            "amount_points": request.data.get("amount_points"),
            "amount_per_point": request.data.get("amount_per_point"),
        }
        serializer = LoyaltySerializer(data=loyality)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, loyality_id, *args, **kwargs):
        loyality = self.get_loyality(loyality_id)
        if not loyality:
            return Response(
                {"res": "Elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        loyality = {
            "amount_points": request.data.get("amount_points"),
            "amount_per_point": request.data.get("amount_per_point"),
            }
        serializer = LoyaltySerializer(loyality, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, loyality_id, *args, **kwargs):
        loyality = self.get_Loyality(loyality_id)
        if not loyality:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        loyality.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
