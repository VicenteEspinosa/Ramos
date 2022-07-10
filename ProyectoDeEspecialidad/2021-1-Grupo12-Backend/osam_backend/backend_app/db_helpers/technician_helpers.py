from backend_app.db_validators.technician_validators import validate_enterprise, validate_team_group
from backend_app.db_validators.form_tree_validators import validate_category
from backend_app.db_models.technician import Technician
from backend_app.db_models.form_tree import FormTree
from backend_app.db_helpers.info_panel_helper import (
    create_info_data
)
from backend_app.db_models.team import Team
from backend_app.db_serializers.technician_serializer import TechnicianSerializer
import logging
import datetime


def send_info_data(technician, auditor_id, technician_status, timestamp):
    if technician_status == "2":
        # edit
        data_type = 1
    else:
        # new
        data_type = 0
    create_info_data(timestamp, 
                     auditor_id, 
                     technician["technician_id"],
                     data_type,
                     0,
                     0)


def complete_technician(data, category, auditor_id, timestamp):
    """The handler for the technician in the answer."""

    number_of_technicians = data['number_of_technicians']
    if number_of_technicians == "1":
        technician = data['technicians']['technician_1']
        data['technicians']['technician_1'] = handle_technician(technician, auditor_id, timestamp)

    elif number_of_technicians == "2":
        technician = data['technicians']['technician_1']
        data['technicians']['technician_1'] = handle_technician(technician, auditor_id, timestamp)
        second_technician = data['technicians']['technician_2']
        data['technicians']['technician_2'] = handle_technician(second_technician, auditor_id, timestamp)
    else:
        logging.error("wrong number_of_technicians")
        raise ValueError("wrong number_of_technicians. Must be '1' or '2' (string).") 

    team_id, id_group_team = get_team_values(data['id_group_team'])
    data['team_id'] = team_id
    data['id_group_team'] = id_group_team
    return data


def handle_technician(technician, auditor_id, timestamp):
    """The handler for the technician in the answer."""

    if technician['status'] == 1:
        technician = get_technician(technician)
    elif technician['status'] == 2:
        technician = patch_technician(technician)
        send_info_data(technician, auditor_id, "2", timestamp)
    elif technician['status'] == 3:
        technician = post_technician(technician)
        send_info_data(technician, auditor_id, "3", timestamp)
    return technician


def post_technician(technician_data):
    """The inside post for a technician."""

    technician_dict = {}
    technician_dict["first_name"] = technician_data["technician_first_name"]
    technician_dict["last_name"] = technician_data["technician_last_name"]
    technician_dict["rut"] = technician_data["technician_rut"]
    technician_dict["enterprise_id"] = technician_data["technician_enterprise_id"]
    technician_dict["phone"] = technician_data["technician_phone"]
    technician_dict["category_id"] = technician_data["technician_category_id"]
    technician_dict["team_group_id"] = technician_data["technician_id_group_team"]
    technician_dict["email"] = technician_data["technician_email"]
    technician_dict["last_audit_date"] = datetime.datetime.now()

    technician_serializer = TechnicianSerializer(data=technician_dict)
    if technician_serializer.is_valid():
        enterprise_id = technician_data['technician_enterprise_id']
        category_id = technician_data['technician_category_id']
        id_group_team = technician_data['technician_id_group_team']
        if validate_enterprise(enterprise_id) and validate_category(category_id) and validate_team_group(id_group_team):
            data = technician_serializer.save()
            data.save()
            first_name = technician_serializer.data["first_name"]
            last_name = technician_serializer.data["last_name"]
            technician_data["technician_name_redes"] = get_technician_name_redes(first_name, last_name)
            technician_data["technician_id"] = technician_serializer.data["id"]
            return technician_data
        else:
            logging.error(f"post_technician error: not valid enterprise_id, category_id or team group id")
    logging.error(f"post_technician error: {technician_serializer.errors}")


def get_technician(technician_data):
    """The inside get for a technician."""

    technician = Technician.objects.get(id=technician_data['technician_id'])
    technician_data['technician_name'] = get_name(technician)
    technician_data['technician_rut'] = technician.rut.replace(".", "")
    technician_data['technician_phone'] = technician.phone
    first_name = technician.first_name
    last_name = technician.last_name
    technician_data["technician_name_redes"] = get_technician_name_redes(first_name, last_name)
    # Update last audit date
    aux_data = TechnicianSerializer(technician).data
    aux_data["last_audit_date"] = datetime.datetime.now()
    technician_serializer = TechnicianSerializer(technician, data=aux_data)
    if technician_serializer.is_valid():
        tech = technician_serializer.save()
        tech.save()
        return technician_data
    else:
        logging.error(f"patch_technician error: {technician_serializer.errors}")


def get_team_values(id_team):
    try:
        team = Team.objects.get(id=id_team)
        team_id = team.code
        id_group_team = team.name
        return team_id, id_group_team

    except Team.DoesNotExist:
        logging.error("The service does not exits")


def patch_technician(technician_data):
    """The inside patch for a technician."""

    technician = Technician.objects.get(id=technician_data['technician_id'])
    aux_data = TechnicianSerializer(technician).data
    aux_data["enterprise_id"] = technician_data["technician_enterprise_id"]
    aux_data["phone"] = technician_data["technician_phone"]
    aux_data["email"] = technician_data["technician_email"]
    aux_data["team_id"] = technician_data["technician_team_id"]
    aux_data["category_id"] = technician_data["technician_category_id"]
    aux_data["team_group_id"] = technician_data["technician_id_group_team"]
    aux_data["last_audit_date"] = datetime.datetime.now()

    technician_serializer = TechnicianSerializer(technician, data=aux_data)
    if technician_serializer.is_valid():
        tech = technician_serializer.save()
        tech.save()
        first_name = technician_serializer.data["first_name"]
        last_name = technician_serializer.data["last_name"]
        technician_data["technician_name_redes"] = get_technician_name_redes(first_name, last_name)
        return technician_data
    logging.error(f"patch_technician error: {technician_serializer.errors}")


def get_name_redes(technician_id):
    technician = Technician.objects.get(id=technician_id)
    if " " in technician.last_name:
        last_names_list = [name.capitalize() for name in technician.last_name.split(" ")]
        last_names = " ".join(last_names_list)
    else:
        last_names = technician.last_name
    if " " in technician.first_name:
        first_names_list = [name.capitalize() for name in technician.first_name.split(" ")]
        first_names = " ".join(first_names_list)
    else:
        first_names = technician.first_name
    return f"{last_names}" + ", " + f"{first_names}"


def get_name(technician):
    """Get Technician name"""

    return f"{technician.first_name} {technician.last_name}"


def check_team_dependencies(team_group):
    """Checks if teams belongs to any technician."""

    allowed_to_delete = True
    technicians_dependency_list = []
    technicians = Technician.objects.filter(team_group_id=team_group.id)
    for technician in technicians:
        allowed_to_delete = False
        technicians_dependency_list.append({"id": technician.id, "rut": technician.rut})
    return (technicians_dependency_list, allowed_to_delete)


def check_enterprise_dependencies(enterprise):
    """Checks if teams belongs to any technician."""

    allowed_to_delete = True
    technicians_dependency_list = []
    technicians = Technician.objects.filter(enterprise_id=enterprise.id)
    for technician in technicians:
        allowed_to_delete = False
        technicians_dependency_list.append({"id": technician.id, "rut": technician.rut})
    return (technicians_dependency_list, allowed_to_delete)


def get_technician_name_redes(first_name, last_name):
    """Generates technician name redes"""

    if " " in last_name:
        last_names_list = [name.capitalize() for name in last_name.split(" ")]
        last_names = " ".join(last_names_list)
    else:
        last_names = last_name

    if " " in first_name:
        first_names_list = [name.capitalize() for name in first_name.split(" ")]
        first_names = " ".join(first_names_list)
    else:
        first_names = first_name

    return f"{last_names}" + ", " + f"{first_names}"
