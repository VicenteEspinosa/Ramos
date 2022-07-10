
from backend_app.db_helpers.form_tree_helpers import get_category_goals, get_categories_active
from backend_app.db_models.answer import Answers
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
import datetime

@api_view(['GET'])
def get_dashboard(_):
    """Returns the Dashboard."""
    # {"0": {"RM": (), "OTHER": ()}...}
    categories = get_categories_active()
    data_dict = {}
    for category in categories:
        category_dict = {} # {RM: (), "OTHER": }
        goal_rm, goal_other = get_category_goals(category)

        today_date = datetime.datetime.today()
        result_date = today_date.replace(day=1)
        result_date = result_date.replace(hour=0, minute=0, second=0, microsecond=0)
        today_date += datetime.timedelta(days=1)

        answers_this_month = Answers.objects.filter(exit_timestamp__gte=result_date,
                                        exit_timestamp__lte=today_date, category_id=category)
        answers_rm_counter = 0
        answers_other_counter = 0
        for answer in answers_this_month:
            if answer.metadata["location_data"]["region"] == "Metropolitana de Santiago":
                answers_rm_counter += 1
            else:
                answers_other_counter += 1
        percentage_rm = (answers_rm_counter / goal_rm) * 100
        if percentage_rm > 100:
            percentage_rm = 100
        percentage_other =  (answers_other_counter / goal_other) * 100
        if percentage_other > 100:
            percentage_other = 100

        category_dict["RM"] = (answers_rm_counter, goal_rm, int(percentage_rm))
        category_dict["OTHER"] = (answers_other_counter, goal_other, int(percentage_other))
        data_dict[category] = category_dict

    return JsonResponse(data_dict, safe=False, status=status.HTTP_200_OK)
