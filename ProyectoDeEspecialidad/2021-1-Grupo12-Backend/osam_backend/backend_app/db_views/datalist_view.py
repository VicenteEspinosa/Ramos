
from backend_app.db_models.datalist import Datalist
from backend_app.db_validators.datalist_validators import (validate_str_list, 
                                                           validate_work_types)

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http.response import JsonResponse


@api_view(['GET'])
def datalist(request):
    """Returns datalist."""

    datalist = Datalist.objects.all().last()
    return JsonResponse(datalist.lists, safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def vehicles(request):
    """Returns all vehicle models from datalist."""

    datalist = Datalist.objects.all().last()
    if request.method == 'GET':
        vehicles = datalist.lists["vehicles"]
        return JsonResponse(vehicles, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        vehicles_data = JSONParser().parse(request)
        if validate_str_list(vehicles_data):
            print("Vehicles validated successfully.")
            datalist.lists["vehicles"] = vehicles_data
            datalist.save()
            return JsonResponse(vehicles_data, safe=False, status=status.HTTP_201_CREATED)
        error = {"error": "Error validating vehicles, data must be list of strings"}
        return JsonResponse(error, safe=False, status=status.HTTP_400_BAD_REQUEST)
  
    error = {"Error": "Invalid request Type."}
    return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def task_types(request):
    """Returns all task_types models from datalist."""

    datalist = Datalist.objects.all().last()
    if request.method == 'GET':
        work_types_data = datalist.lists["task_types"]
        return JsonResponse(work_types_data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        work_types_data = JSONParser().parse(request)
        if validate_work_types(work_types_data):
            datalist.lists["task_types"] = work_types_data
            datalist.save()
            return JsonResponse(work_types_data, safe=False, status=status.HTTP_201_CREATED)
        error = {"error": "Error validating Task types data, "\
                 "keys must be valid categories ids, valeus must be list of strings"}
        return JsonResponse(error, safe=False, status=status.HTTP_400_BAD_REQUEST)
  
    error = {"Error": "Invalid request Type."}
    return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def non_ok_options(request):
    """Returns all vehicle models from datalist."""

    datalist = Datalist.objects.all().last()
    if request.method == 'GET':
        non_ok_options = datalist.lists["non_ok_options"]
        return JsonResponse(non_ok_options, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        non_ok_options = JSONParser().parse(request)
        if validate_str_list(non_ok_options):
            print("Non ok options validated successfully.")
            datalist.lists["non_ok_options"] = non_ok_options
            datalist.save()
            return JsonResponse(non_ok_options, safe=False, status=status.HTTP_201_CREATED)
        error = {"error": "Error validating Non ok options, data must be list of strings"}
        return JsonResponse(error, safe=False, status=status.HTTP_400_BAD_REQUEST)
  
    error = {"Error": "Invalid request Type."}
    return JsonResponse(error, status=status.HTTP_400_BAD_REQUEST)
