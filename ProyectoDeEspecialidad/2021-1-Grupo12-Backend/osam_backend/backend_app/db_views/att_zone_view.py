from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from backend_app.db_models.att_zone import AttZone
from backend_app.db_serializers.att_zone_serializer import AttZoneSerializer
from backend_app.db_helpers.json_helpers import get_indexed_json
from backend_app.db_helpers.location_helpers import check_att_zone_dependencies


@api_view(['GET', 'POST'])
def att_zone_list(request):
    """Returns all the att_zones or add new att_zone"""

    if request.method == 'GET':
        att_zones = AttZone.objects.all()
        att_zone_serializer = AttZoneSerializer(att_zones, many=True)
        return JsonResponse(att_zone_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        zid = 1
        if AttZone.objects.all().count() > 0:
            zid = list(AttZone.objects.all().order_by('-id'))[0].id + 1
        att_zone_data = JSONParser().parse(request)
        att_zone_data["id"] = zid
        att_zone_serializer = AttZoneSerializer(data=att_zone_data)
        if att_zone_serializer.is_valid():
            serializer = att_zone_serializer.save()
            serializer.save()
            return JsonResponse(att_zone_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(att_zone_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def att_zone_list_indexed(request):
    """Returns all the att_zones indexed"""

    if request.method == 'GET':
        att_zones = AttZone.objects.all()
        att_zone_serializer = AttZoneSerializer(att_zones, many=True)
        return JsonResponse(get_indexed_json(att_zone_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def att_zone_detail(request, pk):
    """GET, PUT and DELETE methods for a att_zone."""

    try:
        att_zone = AttZone.objects.get(pk=pk)

        if request.method == 'GET':
            att_zone_serializer = AttZoneSerializer(att_zone)
            return JsonResponse(att_zone_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            att_zone_data = JSONParser().parse(request)
            att_zone_serializer = AttZoneSerializer(att_zone, partial=True, data=att_zone_data)
            if att_zone_serializer.is_valid(raise_exception=True):
                data = att_zone_serializer.save()
                data.save()
                return JsonResponse(att_zone_serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            (communes_dependency_list, allowed_to_delete) = check_att_zone_dependencies(att_zone)
            if allowed_to_delete:
                att_zone.delete()
                return JsonResponse({"deleted": True}, status=status.HTTP_201_CREATED)
            else:
                response = {"deleted": False, "communes": communes_dependency_list}
                return JsonResponse(response, status=status.HTTP_201_CREATED)

    except AttZone.DoesNotExist:
        return JsonResponse({'error': 'The att_zone do not exist'}, status=status.HTTP_404_NOT_FOUND)
