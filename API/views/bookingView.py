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
    def get_Booking(self, booking_id):
        try:
            return Booking.objects.get(id=booking_id)
        except Booking.DoesNotExist:
            return None

    def get(self, request, booking_id, *args, **kwargs):
        booking = self.get_Booking(booking_id)
        if not booking:
            return Response(
                {"res": "La reserva no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = BookingSerializer(booking)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        booking = {
            "check_in": request.data.get("check_in"),
            "check_out": request.data.get("check_out"),
            "client_id": request.data.get("client_id"),
            "parking_id": request.data.get("parking_id"),
            "vehicle_id": request.data.get("vehicle_id")
            }
        serializer = BookingSerializer(data=booking)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, booking_id, *args, **kwargs):
        booking = self.get_Booking(booking_id)
        if not booking:
            return Response(
                {"res": "La reserva no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        booking = {
            "check_in": request.data.get("check_in"),
            "check_out": request.data.get("check_out"),
            "client_id": request.data.get("client_id"),
            "parking_id": request.data.get("parking_id"),
            "vehicle_id": request.data.get("vehicle_id")
            }
        serializer = BookingSerializer(booking, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, booking_id, *args, **kwargs):
        booking = self.get_Booking(booking_id)
        if not booking:
            return Response(
                {"res": "La reserva no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        booking.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
