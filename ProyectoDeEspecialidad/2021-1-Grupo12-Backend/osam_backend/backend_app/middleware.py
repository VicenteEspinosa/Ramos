from backend_app.db_models.user import User
from django.http.response import JsonResponse
from rest_framework import status

permission = {
    2: { # Auditor
        "GET": ["answer", "answers", "answers_indexed", "answers_paginated", "block", "blocks", "blocks_indexed", "categories", "commune", "communes", "communes_indexed", 
                "commune_location", "datalist", "enteprise", "enterprises", "enterprises_indexed", "provinces_indexed", "forms", 
                "form", "forms_indexed", "form_tree", "form_tree_new", "non_ok_options", "provinces", "province", 
                "questions", "questions_indexed", "question", "questions_active", "questions_active_indexed", "questions_active_paginated",
                "region", "regions", "regions_indexed", "task_types", "team", "teams", "teams_indexed","technicians", 
                "technician", "technicians_indexed", "technicians_paginated", "vehicles"],
        "POST": ["answers", "answers_loader", "technicians"]
    },
    3: { # Cliente
        "GET": ["answer", "answers", "answers_indexed", "answers_paginated", "categories", "report", "reports", "reports_by_user_category",
            "report_for_api", "blocks_indexed", "questions_active", "questions_active_indexed", "questions_active_paginated",
            "form_tree", "form_tree_new"],
        "POST": ["generate_report"]
    },
}

no_user_paths = ["generate_report_client_side"]


class SessionMiddleware:
    """Middleware session."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """Call the middleware."""

        path = request.path
        if (path != '/users/login/' and (path.split("/")[1] not in no_user_paths)):
            try:
                model_route = path.split("/")[1]
                access_token = request.META["HTTP_AUTHORIZATION"][7:]
                if access_token != "Null":
                    try:
                        user = User.objects.get(access_token=access_token)     
                    except User.DoesNotExist:
                        try:
                            user = User.objects.get(access_token_mobile=access_token)
                        except User.DoesNotExist:
                            return JsonResponse({"error": "Invalid token"}, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return JsonResponse({"error": "Invalid token: Null"}, status=status.HTTP_401_UNAUTHORIZED)
            except KeyError:
                return JsonResponse({"error": "Invalid token: no token provided"}, status=status.HTTP_401_UNAUTHORIZED)

            if not (user._type == 1 or path == '/users/logout/'):
                no_access_msg = "You dont have access to this endpoint"
                try:
                    not_in_routes = model_route not in permission[user._type][request.method]
                    if not_in_routes:
                        return JsonResponse({"error": no_access_msg}, status=status.HTTP_403_FORBIDDEN)
                except KeyError:
                    return JsonResponse({"error": no_access_msg}, status=status.HTTP_403_FORBIDDEN)
        response = self.get_response(request)
        return response
