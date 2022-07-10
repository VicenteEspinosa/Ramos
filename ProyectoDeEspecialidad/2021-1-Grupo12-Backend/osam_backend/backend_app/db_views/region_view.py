from backend_app.db_helpers.json_helpers import get_indexed_json
from backend_app.db_helpers.location_helpers import check_region_dependencies
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from backend_app.db_models.region import Region
from backend_app.db_serializers.region_serializer import RegionSerializer


@api_view(['GET', 'POST'])
def region_list(request):
    """Returns all the regions and add a new region."""

    if request.method == 'GET':
        regions = Region.objects.all().order_by('name')
        regions_serializer = RegionSerializer(regions, many=True)
        return JsonResponse(regions_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        region_data = JSONParser().parse(request)
        region_serializer = RegionSerializer(data=region_data)
        if region_serializer.is_valid():
            serializer = region_serializer.save()
            serializer.save()
            return JsonResponse(region_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(region_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def region_list_indexed(request):
    """Return all the regions with index."""

    if request.method == 'GET':
        regions = Region.objects.all().order_by('name')
        regions_serializer = RegionSerializer(regions, many=True)
        return JsonResponse(get_indexed_json(regions_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def region_detail(request, pk):
    """The GET, PUT and DELETE method for a region."""

    try:
        region = Region.objects.get(pk=pk)

        if request.method == 'GET':
            region_serializer = RegionSerializer(region)
            return JsonResponse(region_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            region_data = JSONParser().parse(request)
            region_serializer = RegionSerializer(region, partial=True, data=region_data)
            if region_serializer.is_valid(raise_exception=True):
                data = region_serializer.save()
                data.save()
                return JsonResponse(region_serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            (provinces_dependency_list, allowed_to_delete) = check_region_dependencies(region)
            if allowed_to_delete:
                region.delete()
                return JsonResponse({"deleted": True}, status=status.HTTP_201_CREATED)
            else:
                # Region cannot be deleted
                response = {"deleted": False, "provinces": provinces_dependency_list}
                return JsonResponse(response, status=status.HTTP_201_CREATED)

    except Region.DoesNotExist:
        return JsonResponse({'error': 'The region do not exist'}, status=status.HTTP_404_NOT_FOUND)
