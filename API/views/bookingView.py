from rest_framework import viewsets
from API.models.bookingModel import Booking
from API.serializers.bookingSerializer import BookingSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer