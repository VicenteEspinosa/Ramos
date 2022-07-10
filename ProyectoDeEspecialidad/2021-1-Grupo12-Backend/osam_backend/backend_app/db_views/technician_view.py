from backend_app.db_paginators.technician_paginator import TechnicianPaginator
from backend_app.db_models.team import Team
from backend_app.db_validators.technician_validators import validate_enterprise, validate_team_group, validate_phone
from backend_app.db_validators.user_validators import validate_rut
from backend_app.db_validators.form_tree_validators import validate_category
from backend_app.db_models.enterprise import Enterprise
from backend_app.db_models.technician import Technician
from backend_app.db_serializers.technician_serializer import TechnicianSerializer
from backend_app.db_helpers.json_helpers import get_indexed_json
from backend_app.db_helpers.form_tree_helpers import get_categories
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
import datetime


@api_view(['GET'])
def technician_list_paginated(request):
    """GET all technicians or POST a technician."""

    try:
        order_by = request.query_params['order_by']
    except KeyError:
            order_by = 'first_name'

    technicians = Technician.objects.all().order_by(order_by)
    page_size = request.query_params.get('page_size', False)
    if page_size:
        technician_paginator = TechnicianPaginator(page_size)
        response = technician_paginator.generate_response(technicians, TechnicianSerializer, request)
        return response
    return JsonResponse({'error': 'The page_size must be in the path values.'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def technician_list(request):
    """GET all technicians or POST a technician."""

    if request.method == 'GET':
        technicians = Technician.objects.all().order_by('first_name')
        technicians_serializer = TechnicianSerializer(technicians, many=True)
        technicians_data = technicians_serializer.data

        # Get all enterprises
        enterprises = Enterprise.objects.all()
        dict_enterprises = {}
        for enterprise_ in enterprises:
            dict_enterprises[enterprise_.id] = enterprise_.name

        # Get all categories
        dict_categories = get_categories()

        #Get all team groups
        team_groups = Team.objects.all()
        dict_team_groups = {}
        for team_group in team_groups:
            dict_team_groups[team_group.id] = {
                'code': team_group.code,
                'name': team_group.name
            }

        for technician in technicians_data:
            try:
                technician['enterprise_name'] = dict_enterprises[technician['enterprise_id']]
                technician['category_name'] = dict_categories[str(technician['category_id'])]
                technician['team_group_code'] = dict_team_groups[technician['team_group_id']]['code']
                technician['team_group_name'] = dict_team_groups[technician['team_group_id']]['name']
            except KeyError:
                technician_error = {"error": "The enterprise or category no longer exists."}
                return JsonResponse(technician_error, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(technicians_data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        technician_data = JSONParser().parse(request)
        technician_data['last_audit_date'] = datetime.datetime.now()
        technician_serializer = TechnicianSerializer(data=technician_data)

        if technician_serializer.is_valid():
            enterprise_id = technician_data['enterprise_id']
            category_id = technician_data['category_id']
            team_group_id = technician_data['team_group_id']
            rut = technician_data['rut']
            phone = technician_data['phone']

            if validate_enterprise(enterprise_id) \
                and validate_category(category_id) \
                    and validate_team_group(team_group_id) \
                        and validate_rut(rut) and validate_phone(phone):
                data = technician_serializer.save()
                data.save()
                return JsonResponse(technician_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse({"error": "The ids, phone or rut given are not valid."}, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(technician_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def technician_list_indexed(request):
    """Returns all technicians with their index."""

    try:
        order_by = request.query_params['order_by']
    except KeyError:
        order_by = 'first_name'

    technicians = Technician.objects.all().order_by(order_by)
    technicians_serializer = TechnicianSerializer(technicians, many=True)
    technicians_data = technicians_serializer.data

    # Get all enterprises
    enterprises = Enterprise.objects.all()
    dict_enterprises = {}
    for enterprise_ in enterprises:
        dict_enterprises[enterprise_.id] = enterprise_.name

    # Get all categories
    dict_categories = get_categories()

    # Get all team groups
    team_groups = Team.objects.all()
    dict_team_groups = {}
    for team_group in team_groups:
        dict_team_groups[team_group.id] = {
            'code': team_group.code,
            'name': team_group.name
        }

    for technician in technicians_data:
        try:
            technician['enterprise_name'] = dict_enterprises[technician['enterprise_id']]
            technician['category_name'] = dict_categories[str(technician['category_id'])]
            technician['team_group_code'] = dict_team_groups[technician['team_group_id']]['code']
            technician['team_group_name'] = dict_team_groups[technician['team_group_id']]['name']
        except KeyError:
            technician_error = {"error": "The enterprise, category or team group no longer exists."}
            return JsonResponse(technician_error, status=status.HTTP_404_NOT_FOUND)
    return JsonResponse(get_indexed_json(technicians_data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def technician_by_category(request, category_id):
    """Returns all technicians with with category_id=category_id"""
    technicians = Technician.objects.filter(category_id=category_id)
    technicians_serializer = TechnicianSerializer(technicians, many=True)
    technicians_data = technicians_serializer.data

    # Get all enterprises
    enterprises = Enterprise.objects.all()
    dict_enterprises = {}
    for enterprise_ in enterprises:
        dict_enterprises[enterprise_.id] = enterprise_.name

    # Get all categories
    dict_categories = get_categories()

    # Get all team groups
    team_groups = Team.objects.all()
    dict_team_groups = {}
    for team_group in team_groups:
        dict_team_groups[team_group.id] = {
            'code': team_group.code,
            'name': team_group.name
        }

    for technician in technicians_data:
        try:
            technician['enterprise_name'] = dict_enterprises[technician['enterprise_id']]
            technician['category_name'] = dict_categories[str(technician['category_id'])]
            technician['team_group_code'] = dict_team_groups[technician['team_group_id']]['code']
            technician['team_group_name'] = dict_team_groups[technician['team_group_id']]['name']
        except KeyError as ex:
            technician_error = {"error": "The enterprise, category or team group no longer exists."}
            return JsonResponse(technician_error, status=status.HTTP_404_NOT_FOUND)
    return JsonResponse(technicians_data, safe=False, status=status.HTTP_200_OK)


@api_view(['GET'])
def technician_indexed_by_category(request, category_id):
    """Returns all technicians with their index with category_id = category_id."""

    technicians = Technician.objects.filter(category_id=category_id)
    technicians_serializer = TechnicianSerializer(technicians, many=True)
    technicians_data = technicians_serializer.data

    # Get all enterprises
    enterprises = Enterprise.objects.all()
    dict_enterprises = {}
    for enterprise_ in enterprises:
        dict_enterprises[enterprise_.id] = enterprise_.name

    # Get all categories
    dict_categories = get_categories()

    # Get all team groups
    team_groups = Team.objects.all()
    dict_team_groups = {}
    for team_group in team_groups:
        dict_team_groups[team_group.id] = {
            'code': team_group.code,
            'name': team_group.name
        }

    for technician in technicians_data:
        try:
            technician['enterprise_name'] = dict_enterprises[technician['enterprise_id']]
            technician['category_name'] = dict_categories[str(technician['category_id'])]
            technician['team_group_code'] = dict_team_groups[technician['team_group_id']]['code']
            technician['team_group_name'] = dict_team_groups[technician['team_group_id']]['name']
        except KeyError:
            technician_error = {"error": "The enterprise, category or team group no longer exists."}
            return JsonResponse(technician_error, status=status.HTTP_404_NOT_FOUND)
    return JsonResponse(get_indexed_json(technicians_data), safe=False, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def technician_detail(request, pk):
    """GET, PUT or DELETE a technician."""

    try:
        technician = Technician.objects.get(pk=pk)

        if request.method == 'GET':
            technician_serializer = TechnicianSerializer(technician)

            # Get the extenal info
            enterprise = Enterprise.objects.get(id=technician_serializer.data['enterprise_id'])
            team_group = Team.objects.get(id=technician_serializer.data['team_group_id'])
            categories = get_categories()

            technician_data = technician_serializer.data
            technician_data['enterprise_name'] = enterprise.name
            technician_data['category_name'] = categories[str(technician.category_id)]
            technician_data['team_group_code'] = team_group.code
            technician_data['team_group_name'] = team_group.name
            return JsonResponse(technician_data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            technician_data = JSONParser().parse(request)
            technician_serializer = TechnicianSerializer(technician, data=technician_data)

            if technician_serializer.is_valid():
                enterprise_id = technician_data['enterprise_id']
                category_id = technician_data['category_id']
                team_group_id = technician_data['team_group_id']
                rut = technician_data['rut']
                phone = technician_data['phone']

                if validate_enterprise(enterprise_id) \
                    and validate_category(category_id) \
                        and validate_team_group(team_group_id) \
                            and validate_rut(rut) and validate_phone(phone):
                    data = technician_serializer.save()
                    data.enterprise_id = enterprise_id
                    data.category_id = category_id
                    data.team_group_id = team_group_id
                    data.rut = rut
                    data.save()
                    return JsonResponse(technician_serializer.data, status=status.HTTP_201_CREATED)
                technician_error = {"error": "The ids, phone or rut given are not valid."}
                return JsonResponse(technician_error, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse(technician_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE': 
            technician.delete()
            return JsonResponse({'message': 'Technician was deleted successfully!'}, status=status.HTTP_201_CREATED)

    except Technician.DoesNotExist:
        return JsonResponse({'message': 'Technician does not exist.'})
