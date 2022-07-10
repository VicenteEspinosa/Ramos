from backend_app.db_helpers.form_tree_helpers import get_categories
from rest_framework import status
from rest_framework.exceptions import NotFound as NotFoundError
from rest_framework.pagination import PageNumberPagination # Any other type works as well
from rest_framework.response import Response
from backend_app.db_models.enterprise import Enterprise
from backend_app.db_models.team import Team
from backend_app.db_models.technician import Technician
import math

class TechnicianPaginator(PageNumberPagination):

    def __init__(self, page_size) -> None:
        super().__init__()
        self.page_size = page_size # Number of objects to return in one page
        self.last_page = 0 # The last page that you can access


    def generate_response(self, query_set, serializer_obj, request):
        technician_count = Technician.objects.all().count()
        self.last_page = math.ceil(technician_count / int(self.page_size))

        try:
            page_data = self.paginate_queryset(query_set, request)
        except NotFoundError:
            return Response({'length_error': int(self.last_page)}, status=status.HTTP_400_BAD_REQUEST)

        serialized_page = serializer_obj(page_data, many=True)

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

        for technician in serialized_page.data:
            try:
                technician['enterprise_name'] = dict_enterprises[technician['enterprise_id']]
                technician['category_name'] = dict_categories[str(technician['category_id'])]
                technician['team_group_code'] = dict_team_groups[technician['team_group_id']]['code']
                technician['team_group_name'] = dict_team_groups[technician['team_group_id']]['name']
            except KeyError as ex:
                technician_error = {"error": "The enterprise or category no longer exists."}
                return Response(technician_error, status=status.HTTP_404_NOT_FOUND)

        data = serialized_page.data # add the get_indexed_json here
        return self.get_paginated_response(data)


    def get_paginated_response(self, data):
        return Response({

            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'page_size': int(self.page_size),
            'last_page': self.last_page,
            'data': data
        })
