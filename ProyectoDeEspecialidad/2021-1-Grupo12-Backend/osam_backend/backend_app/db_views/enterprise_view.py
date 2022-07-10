from backend_app.db_helpers.technician_helpers import check_enterprise_dependencies
from backend_app.db_models.enterprise import Enterprise
from backend_app.db_serializers.enterprise_serializer import EnterpriseSerializer
from backend_app.db_helpers.json_helpers import get_indexed_json
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
def enterprise_list(request):
    """Returns all the enterprises or add a new enterprise."""

    if request.method == 'GET':
        enterprises = Enterprise.objects.all().order_by('name')
        enterprises_serializer = EnterpriseSerializer(enterprises, many=True)
        return JsonResponse(enterprises_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        enterprise_data = JSONParser().parse(request)
        enterprise_serializer = EnterpriseSerializer(data=enterprise_data)
        if enterprise_serializer.is_valid():
            data = enterprise_serializer.save()
            data.save()
            return JsonResponse(enterprise_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(enterprise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def enterprise_list_indexed(request):
    """Return all the enterprises with index."""

    if request.method == 'GET':
        enterprises = Enterprise.objects.all().order_by('name')
        enterprises_serializer = EnterpriseSerializer(enterprises, many=True)
        return JsonResponse(get_indexed_json(enterprises_serializer.data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PATCH', 'DELETE'])
def enterprise_detail(request, pk):
    """The GET, PATCH and DELETE method for a enterprise."""

    try:
        enterprise = Enterprise.objects.get(pk=pk)

        if request.method == 'GET':
            enterprise_serializer = EnterpriseSerializer(enterprise)
            return JsonResponse(enterprise_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            enterprise_data = JSONParser().parse(request)
            enterprise_serializer = EnterpriseSerializer(enterprise, partial= True, data=enterprise_data)
            if enterprise_serializer.is_valid(raise_exception=True):
                data = enterprise_serializer.save()
                data.save()
            return JsonResponse(enterprise_serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            (technicians_dependency_list, allowed_to_delete) = check_enterprise_dependencies(enterprise)
            if allowed_to_delete:
                enterprise.delete()
                return JsonResponse({"deleted": True}, status=status.HTTP_201_CREATED)
            else:
                # Enterprise cannot be deleted
                response = {"deleted": False, "technicians": technicians_dependency_list}
                return JsonResponse(response, status=status.HTTP_201_CREATED)

    except Enterprise.DoesNotExist:
        return JsonResponse({'error': 'The enterprise do not exist'}, status=status.HTTP_404_NOT_FOUND)
