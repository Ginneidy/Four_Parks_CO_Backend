from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db import transaction
from helpers.helpers import get_current_datetime


class BaseViewSet(viewsets.ModelViewSet):
    queryset = None
    serializer_class = None

    def create(self, request, *args, **kwargs):
        """
        Create a new instance.

        Returns:
            Response: HTTP response with created instance data or error messages.
        """
        created_date = get_current_datetime()

        with transaction.atomic():
            serializer = self.serializer_class(data=request.data)

            if serializer.is_valid():
                serializer.save(created_date=created_date)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    {"error": "Invalid data provided"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

    def update(self, request, *args, **kwargs):
        """
        Update an existing instance.

        Returns:
            Response: HTTP response with updated instance data or error messages.
        """

        data = request.data
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=data, partial=True)

        with transaction.atomic():
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(
                    {"error": "Invalid data provided"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

    def destroy(self, request, *args, **kwargs):
        """
        Soft delete an existing instance.

        Returns:
            Response: HTTP response indicating successful deletion or error.
        """

        instance = self.get_object()
        instance.deleted_date = get_current_datetime()
        instance.save()
        return Response(
            {"message": f"{self.queryset.model.__name__} deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )
