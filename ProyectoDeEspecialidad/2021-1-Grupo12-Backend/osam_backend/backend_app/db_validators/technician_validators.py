from backend_app.db_models.team import Team
from backend_app.db_models.enterprise import Enterprise
from backend_app.db_helpers.answer_keys import (
    TECHNICIAN_KEYS,
    TECHNICIANS_KEYS
)
MAX_TECHNICINAS = 2
VALID_TECHNICIANS_STATUS = [0, 1, 2, 3]


def validate_technicians(technician_data):
    """The technicians validations for an answer."""

    if type(technician_data) != dict:
        return False 
    else:
        keys = technician_data.keys()
        if len(keys) != len(TECHNICIANS_KEYS):
            return False
        for key in keys:
            if key == "technicians":
                technicians = technician_data["technicians"]
                if type(technicians) != dict:
                    return False
                if len(technicians) != MAX_TECHNICINAS:
                    return False 
                for tech in technicians.values():
                    if not validate_technician(tech):
                        return False

            elif key not in TECHNICIANS_KEYS:
                return False
            elif type(technician_data[key]) != str:
                return False
    return True


def validate_technician(technician: dict) -> bool:
    """The technician validation for an answer."""

    if type(technician) != dict:
        return False
    if len(technician.keys()) != len(TECHNICIAN_KEYS):
        return False
    for key in technician:
        if key not in TECHNICIAN_KEYS:
            return False
        value = technician[key]
        if key == "technician_id":
            if type(value) != int:
                return False
        elif key == "status":
            if value not in VALID_TECHNICIANS_STATUS:
                return False
        else:
            if type(value) != str:
                return False
    return True


def validate_enterprise(enterprise_id):
    """Validate if the enterprise exists."""

    try:
        Enterprise.objects.get(pk=enterprise_id)
        return True

    except Enterprise.DoesNotExist:
        return False


def validate_team_group(team_group_id):
    """Validate if the team group exists."""

    try:
        Team.objects.get(pk=team_group_id)
        return True

    except Team.DoesNotExist:
        return False

def validate_phone(phone):
    # Allow Empty phones
    if not phone:
        return True
    
    if not phone.isnumeric():
        return False
    
    if (len(phone) > 12) or (len(phone) < 9):
        return False
    
    return True
