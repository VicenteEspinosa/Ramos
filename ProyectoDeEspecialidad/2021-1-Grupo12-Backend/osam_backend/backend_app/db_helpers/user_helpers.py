from backend_app.db_models.user import User

def get_auditor(auditor_id, auditor_data):
    """Returns the auditor with a specific structure."""

    user = User.objects.get(user_id=auditor_id)
    auditor_data["auditor_name"] = f"{user.first_name} {user.last_name}"
    auditor_data["auditor_rut"] = user.rut
    auditor_data["auditor_email"] = user.email
    auditor_data["auditor_phone"] = "56900000000"
    return auditor_data


def get_indexed_json_user(user_data):
    """Returns the user data with the index outside."""

    indexed_data = {}
    keys = [i["user_id"] for i in user_data]
    for i, j in enumerate(keys):
        indexed_data[j] = user_data[i]
    return indexed_data

def userid_type_category_by_request(request):
    access_token = request.META["HTTP_AUTHORIZATION"][7:]
    try:
        user = User.objects.get(access_token=access_token)
    except User.DoesNotExist:
        user = User.objects.get(access_token_mobile=access_token)
    return user.user_id, user._type, user.category_id

def get_current_user(request):
    access_token = request.META["HTTP_AUTHORIZATION"][7:]
    try:
        user = User.objects.get(access_token=access_token)
    except User.DoesNotExist:
        user = User.objects.get(access_token_mobile=access_token)
    return user