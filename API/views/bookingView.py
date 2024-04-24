from rest_framework import viewsets
from API.models.bookingModel import Booking 
from API.serializers.bookingSerializer import BookingSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    def get_Booking(self, Booking_id):
        try:
            return Booking.objects.get(id=Booking_id)
        except Booking.DoesNotExist:
            return None

'''    def get(self, request, Booking_id, *args, **kwargs):
        booking = self.get_User(Booking_id)
        if not booking:
            return Response(
                {"res": "La reserva no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        booking = {
            "date": request.data.get("date"),
            "client_id": request.data.get("client_id"),
            "parking_id": request.data.get("parking_id"),
            "vehicle_id": request.data.get("vehicle_id")
            }
        serializer = BookingSerializer(data=booking)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id, *args, **kwargs):
        user = self.get_user(user_id)
        if not user:
            return Response(
                {"res": "El usuario no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        user = {
            "name": request.data.get("name"),
            "last_name": request.data.get("last_name"),
            "username": request.data.get("username"),
            "email_address": request.data.get("email_address"),
            "password": request.data.get("password"),
            "document_type": request.data.get("document_type"),
            "document": request.data.get("document"),}
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, user_id, *args, **kwargs):
        user = self.get_User(user_id)
        if not user:
            return Response(
                {"res": "El elemento no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        user.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
'''