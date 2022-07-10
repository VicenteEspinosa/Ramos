from backend_app.db_models.info_panel import InfoPanel
from backend_app.db_serializers.info_panel_serializer import InfoPanelSerializer
from backend_app.db_helpers.json_helpers import get_indexed_json

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'DELETE'])
def info_panel_indexed(request):
    """Return all the info panel data with index."""

    if request.method == 'GET':
        infopanel_data = InfoPanel.objects.all()
        infopanel_serializer = InfoPanelSerializer(infopanel_data, many=True)
        return JsonResponse(get_indexed_json(infopanel_serializer.data), safe=False, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        try:
            delete_timestamp_data = JSONParser().parse(request)
            delete_timestamp = delete_timestamp_data["timestamp"]
            infopanel_filtered = InfoPanel.objects.filter(timestamp__lte=delete_timestamp)
            for infodata in infopanel_filtered:
                infodata.delete()
            msg = {"deleted": f"All info data before {delete_timestamp} was deleted successfully"}
            return JsonResponse(msg, safe=False, status=status.HTTP_200_OK)
        except (TypeError, ValidationError, KeyError) as Error:
            t_error = {"Error": str(Error)}
            return JsonResponse(t_error, safe=False, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"error": "bad request"}, safe=False, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['DELETE'])
def infopaneldata_detail(request, pk):
    """The GET, PUT and DELETE method for an answer."""

    try:
        infodata = InfoPanel.objects.get(pk=pk)            
        infodata.delete()
        return JsonResponse({"deleted": True}, status=status.HTTP_200_OK)

    except InfoPanel.DoesNotExist:
        return JsonResponse({'error': 'The info panel data does not exist'}, status=status.HTTP_404_NOT_FOUND)
    