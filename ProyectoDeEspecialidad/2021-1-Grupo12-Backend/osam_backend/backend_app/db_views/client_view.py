from backend_app.db_helpers.json_helpers import get_indexed_json
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from backend_app.db_models.client import Client
from backend_app.db_serializers.client_serializer import ClientSerializer, ClientPatchSerializer


@api_view(['GET'])
def client_list(request):
    """Return all the clients with index."""

    if request.method == 'GET':
        clients = Client.objects.all()
        clients_serializer = ClientSerializer(clients, many=True)
        return JsonResponse(get_indexed_json(clients_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH'])
def client_detail(request, pk):
    """The GET and PATCH method for a client."""

    try:
        client = Client.objects.get(pk=pk)

        if request.method == 'GET':
            client_serializer = ClientSerializer(client)
            return JsonResponse(client_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            client_data = JSONParser().parse(request)
            client_serializer = ClientPatchSerializer(client, partial=True, data=client_data)
            if client_serializer.is_valid(raise_exception=True):
                data = client_serializer.save()
                data.save()
            return JsonResponse(client_serializer.data, status=status.HTTP_201_CREATED)

    except Client.DoesNotExist:
        return JsonResponse({'error': 'The client does not exist'}, status=status.HTTP_404_NOT_FOUND)
