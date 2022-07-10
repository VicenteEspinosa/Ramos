from backend_app.db_helpers.technician_helpers import check_team_dependencies
from backend_app.db_models.team import Team
from backend_app.db_serializers.team_serializer import TeamSerializer
from backend_app.db_helpers.json_helpers import get_indexed_json
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser


@api_view(['GET', 'POST'])
def team_list(request):
    """Returns all the teams."""

    if request.method == 'GET':
        teams = Team.objects.all().order_by('name')
        team_serializer = TeamSerializer(teams, many=True)
        return JsonResponse(team_serializer.data, safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        team_data = JSONParser().parse(request)
        team_id = 1
        if Team.objects.all().count() > 0:
            team_id = list(Team.objects.all().order_by('-id'))[0].id + 1
        team_data["id"] = team_id
        team_serializer = TeamSerializer(data=team_data)
        if team_serializer.is_valid():
            serializer = team_serializer.save()
            serializer.save()
            return JsonResponse(team_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(team_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def team_detail(request, pk):
    """The GET, PUT and DELETE method for a team group."""

    try:
        team = Team.objects.get(pk=pk)

        if request.method == 'GET':
            team_serializer = TeamSerializer(team)
            return JsonResponse(team_serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PATCH':
            team_data = JSONParser().parse(request)
            team_serializer = TeamSerializer(team, partial= True, data=team_data)
            team_serializer.is_valid(raise_exception=True)
            team_serializer.save()
            return JsonResponse(team_serializer.data, status=status.HTTP_201_CREATED)

        elif request.method == 'DELETE':
            (technicians_dependency_list, allowed_to_delete) = check_team_dependencies(team)
            if allowed_to_delete:
                team.delete()
                return JsonResponse({"deleted": True}, status=status.HTTP_201_CREATED)
            else:
                # Team group cannot be deleted
                response = {"deleted": False, "technicians": technicians_dependency_list}
                return JsonResponse(response, status=status.HTTP_201_CREATED)

    except Team.DoesNotExist:
        return JsonResponse({'error': 'The team group do not exist'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def team_list_indexed(request):
    """Returns all the team groups."""

    teams = Team.objects.all().order_by('name')
    team_serializer = TeamSerializer(teams, many=True)
    return JsonResponse(get_indexed_json(team_serializer.data), safe=False, status=status.HTTP_200_OK)
