from backend_app.db_helpers.json_helpers import get_indexed_json
from backend_app.db_helpers.location_helpers import check_province_dependencies
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from django.http.response import JsonResponse
from backend_app.db_models.province import Province
from backend_app.db_serializers.province_serializer import ProvinceSerializer


@api_view(['GET', 'POST'])
def province_list(request):
    """Returns all the provinces and add a new province."""

    if request.method == 'GET':
        provinces = Province.objects.all().order_by('name')
        provinces_serializer = ProvinceSerializer(provinces, many=True)
        return JsonResponse(provinces_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        province_data = JSONParser().parse(request)
        province_serializer = ProvinceSerializer(data=province_data)
        if province_serializer.is_valid():
            serializer = province_serializer.save()
            serializer.save()
            return JsonResponse(province_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(province_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def province_list_indexed(request):
    """Return all the provinces with index."""

    if request.method == 'GET':
        provinces = Province.objects.all().order_by('name')
        provinces_serializer = ProvinceSerializer(provinces, many=True)
        return JsonResponse(get_indexed_json(provinces_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def province_detail(request, pk):
    """The GET, PATCH and DELETE method for a province."""

    try:
        province = Province.objects.get(pk=pk)

        if request.method == 'GET':
            province_serializer = ProvinceSerializer(province)
            return JsonResponse(province_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            province_data = JSONParser().parse(request)
            province_serializer = ProvinceSerializer(province, partial= True, data=province_data)
            if province_serializer.is_valid(raise_exception=True):
                data = province_serializer.save()
                data.save()
            return JsonResponse(province_serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            (communes_dependency_list, allowed_to_delete) = check_province_dependencies(province)
            if allowed_to_delete:
                province.delete()
                return JsonResponse({"deleted": True}, status=status.HTTP_201_CREATED)
            else:
                # Province cannot be deleted
                response = {"deleted": False, "communes": communes_dependency_list}
                return JsonResponse(response, status=status.HTTP_201_CREATED)

    except Province.DoesNotExist:
        return JsonResponse({'error': 'The province do not exist'}, status=status.HTTP_404_NOT_FOUND)
