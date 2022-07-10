from backend_app.db_helpers.json_helpers import get_indexed_json
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from backend_app.db_models.commune import Commune
from backend_app.db_models.att_zone import AttZone
from backend_app.db_models.crmzone import CrmZone
from backend_app.db_serializers.commune_serializer import CommuneSerializer
from backend_app.db_serializers.province_serializer import ProvinceSerializer
from backend_app.db_serializers.region_serializer import RegionSerializer
from backend_app.db_serializers.att_zone_serializer import AttZoneSerializer
from backend_app.db_serializers.crmzone_serializer import CrmZoneSerializer
from backend_app.db_helpers.location_helpers import get_province, get_region


@api_view(['GET', 'POST'])
def commune_list(request):
    """Returns all the communes."""

    if request.method == 'GET':
        communes = Commune.objects.all().order_by('name')
        communes_serializer = CommuneSerializer(communes, many=True)
        return JsonResponse(communes_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        commune_data = JSONParser().parse(request)
        commune_serializer = CommuneSerializer(data=commune_data)
        if commune_serializer.is_valid():
            serializer = commune_serializer.save()
            serializer.save()
            return JsonResponse(commune_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(commune_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def commune_location(request, pk):
    """Returns the province ,region, att_zone and crmzone this communes belongs to."""

    try:
        commune = Commune.objects.get(pk=pk)
        commune_serializer = CommuneSerializer(commune)

        # Get att_zone
        try:
            att_zone = AttZone.objects.get(pk=commune_serializer.data['region_zona_att'])
            att_zone_serializer = AttZoneSerializer(att_zone)
        except AttZone.DoesNotExist:
            return JsonResponse({'error': 'Could not find commune region_zona_att'}, status=status.HTTP_404_NOT_FOUND)

        # Get crmzone
        try:
            crmzone = CrmZone.objects.get(pk=commune_serializer.data['region_crm'])
            crmzone_serializer = CrmZoneSerializer(crmzone)
        except CrmZone.DoesNotExist:
            return JsonResponse({'error': 'Could not find commune region_crm'}, status=status.HTTP_404_NOT_FOUND)

        # Fill json_data with commune data
        json_data = {}
        json_data['commune_id'] = commune_serializer.data['id']
        json_data['commune_name'] = commune_serializer.data['name']
        json_data['region_zona_att'] = att_zone_serializer.data['name'] 
        json_data['region_crm'] = crmzone_serializer.data['name']

        province = get_province(commune.province_id)
        region = get_region(province.region_id)
        if province is not None and region is not None:
            province_serializer = ProvinceSerializer(province)
            region_serializer = RegionSerializer(region)

            # Fill json data with province and region data
            json_data['province_name'] = province_serializer.data['name']
            json_data['province_id'] = province_serializer.data['id']
            json_data['region_name'] = region_serializer.data['name']
            json_data['region_id'] = region_serializer.data['id']
            return JsonResponse(json_data, status=status.HTTP_200_OK)

        return JsonResponse({'error': 'Could not find province and region'}, status=status.HTTP_200_OK)
    except Commune.DoesNotExist:
        return JsonResponse({'error': 'The commune do not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def commune_list_indexed(request):
    """Return all the communes with index."""

    if request.method == 'GET':
        communes = Commune.objects.all().order_by('name')
        communes_serializer = CommuneSerializer(communes, many=True)
        return JsonResponse(get_indexed_json(communes_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def commune_detail(request, pk):
    """The GET, PUT and DELETE method for a commune."""

    try:
        commune = Commune.objects.get(pk=pk)

        if request.method == 'GET':
            commune_serializer = CommuneSerializer(commune)
            return JsonResponse(commune_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            commune_data = JSONParser().parse(request)
            commune_serializer = CommuneSerializer(commune, partial=True, data=commune_data)
            if commune_serializer.is_valid(raise_exception=True):
                data = commune_serializer.save()
                data.save()
            return JsonResponse(commune_serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            commune.delete()
            return JsonResponse({"deleted": True}, status=status.HTTP_201_CREATED)
    except Commune.DoesNotExist:
        return JsonResponse({'error': 'The commune do not exist'}, status=status.HTTP_404_NOT_FOUND)
