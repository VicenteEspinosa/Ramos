from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from backend_app.db_models.crmzone import CrmZone
from backend_app.db_serializers.crmzone_serializer import CrmZoneSerializer
from backend_app.db_helpers.json_helpers import get_indexed_json
from backend_app.db_helpers.location_helpers import check_crmzone_dependencies


@api_view(['GET', 'POST'])
def crmzone_list(request):
    """Returns all the crmzones or add new crmzone"""

    if request.method == 'GET':
        crmzones = CrmZone.objects.all()
        crmzone_serializer = CrmZoneSerializer(crmzones, many=True)
        return JsonResponse(crmzone_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        zid = 1
        if CrmZone.objects.all().count() > 0:
            zid = list(CrmZone.objects.all().order_by('-id'))[0].id + 1
        crmzone_data = JSONParser().parse(request)
        crmzone_data["id"] = zid
        crmzone_serializer = CrmZoneSerializer(data=crmzone_data)
        if crmzone_serializer.is_valid():
            serializer = crmzone_serializer.save()
            serializer.save()
            return JsonResponse(crmzone_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(crmzone_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def crmzone_list_indexed(request):
    """Returns all the crmzones indexed"""

    if request.method == 'GET':
        crmzones = CrmZone.objects.all()
        crmzone_serializer = CrmZoneSerializer(crmzones, many=True)
        return JsonResponse(get_indexed_json(crmzone_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def crmzone_detail(request, pk):
    """GET, PUT and DELETE methods for a crmzone."""

    try:
        crmzone = CrmZone.objects.get(pk=pk)

        if request.method == 'GET':
            crmzone_serializer = CrmZoneSerializer(crmzone)
            return JsonResponse(crmzone_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            crmzone_data = JSONParser().parse(request)
            crmzone_serializer = CrmZoneSerializer(crmzone, partial=True, data=crmzone_data)
            if crmzone_serializer.is_valid(raise_exception=True):
                data = crmzone_serializer.save()
                data.save()
                return JsonResponse(crmzone_serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            (communes_dependency_list, allowed_to_delete) = check_crmzone_dependencies(crmzone)
            check_crmzone_dependencies(crmzone)
            if allowed_to_delete:
                crmzone.delete()
                return JsonResponse({"deleted": True}, status=status.HTTP_201_CREATED)
            else:
                response = {"deleted": False, "communes": communes_dependency_list}
                return JsonResponse(response, status=status.HTTP_201_CREATED)

    except CrmZone.DoesNotExist:
        return JsonResponse({'error': 'The crmzone do not exist'}, status=status.HTTP_404_NOT_FOUND)
