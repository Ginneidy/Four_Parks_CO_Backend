from rest_framework import viewsets
from Apps.reservation_billing.models import Booking,PaymentMethod,Bill,CreditCard
from Apps.vehicle.models import Vehicle
from Apps.reservation_billing.serializers import BookingSerializer,PaymentMethodSerializer,BillSerializer,CreditCardSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

# Create your views here.


class BookingViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
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
    
class PaymentMethodViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer
    def get_PaymentMethod(self, PaymentMethod_id):
        try:
            return PaymentMethod.objects.get(id=PaymentMethod_id)
        except PaymentMethod.DoesNotExist:
            return None

    def get(self, request, PaymentMethod_id, *args, **kwargs):
        PaymentMethod = self.get_PaymentMethod(PaymentMethod_id)
        if not PaymentMethod:
            return Response(
                {"res": "El metodo de pago no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = PaymentMethodSerializer(PaymentMethod)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        PaymentMethod = {
            "description": request.data.get("description")
        }
        serializer = PaymentMethodSerializer(data=PaymentMethod)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, PaymentMethod_id, *args, **kwargs):
        PaymentMethod = self.get_PaymentMethod(PaymentMethod_id)
        if not PaymentMethod:
            return Response(
                {"res": "El metodo de pago no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        PaymentMethod = {
            "description": request.data.get("description")
        }
        serializer = PaymentMethodSerializer(PaymentMethod, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, PaymentMethod_id, *args, **kwargs):
        PaymentMethod = self.get_PaymentMethod(PaymentMethod_id)
        if not PaymentMethod:
            return Response(
                {"res": "El metodo de pago no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        PaymentMethod.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK)
            
class BillViewSet(viewsets.ModelViewSet):
    #permission_classes = [permissions.IsAuthenticated]
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    
    def get_Bill(self, Bill_id):
        try:
            return Bill.objects.get(id=Bill_id)
        except Bill.DoesNotExist:
            return None

    def get(self, request, Bill_id, *args, **kwargs):
        Bill = self.get_Bill(Bill_id)
        if not Bill:
            return Response(
                {"res": "La cuenta no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = BillSerializer(Bill)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        user = request.user
        Bill = {
            "code": request.data.get("code"),
            "vehicle_entry": request.data.get("vehicle_entry"),
            "vehicle_exit": request.data.get("vehicle_exit"),
            "total_time": request.data.get("total_time"),
            "points_used": request.data.get("points_used"),
            "total_amount": request.data.get("total_amount"),
            "booking_id": request.data.get("booking_id"),
            "payment_method_id": request.data.get("payment_method_id")
        }
        serializer = BillSerializer(data=Bill)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, Bill_id, *args, **kwargs):
        Bill = self.get_Bill(Bill_id)
        if not Bill:
            return Response(
                {"res": "La cuenta no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        Bill = {
            "code": request.data.get("code"),
            "vehicle_entry": request.data.get("vehicle_entry"),
            "vehicle_exit": request.data.get("vehicle_exit"),
            "total_time": request.data.get("total_time"),
            "points_used": request.data.get("points_used"),
            "total_amount": request.data.get("total_amount"),
            "booking_id": request.data.get("booking_id"),
            "payment_method_id": request.data.get("payment_method_id")
        }
        serializer = BillSerializer(Bill, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, resquest, Bill_id, *args, **kwargs):
        Bill = self.get_Bill(Bill_id)
        if not Bill:
            return Response(
                {"res": "La cuenta no existe"}, status=status.HTTP_404_NOT_FOUND
            )
        Bill.delete()
        return Response({"res": "Elemento eliminado"}, status=status.HTTP_200_OK) 
            