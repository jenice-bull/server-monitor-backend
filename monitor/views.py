from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils.monitor import get_server_status

@api_view(['GET'])
def server_status(request):
    data = get_server_status()
    return Response(data)
