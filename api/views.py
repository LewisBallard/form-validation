from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.serializers import CreateAccountSerializer


@api_view(['POST'])
def create_account(request):
    """
    Basic view that validates the passed in fields.
    """
    serializer = CreateAccountSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.data)
