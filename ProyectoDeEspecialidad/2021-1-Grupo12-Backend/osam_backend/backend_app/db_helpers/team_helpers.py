from backend_app.db_models.team import Team


def get_team(team_id):
    """Return the team id and the id group team."""

    team = Team.objects.get(pk=team_id)
    data = {
        "team_id": team.code,
        "id_group_team": team.name
    }
    return data
