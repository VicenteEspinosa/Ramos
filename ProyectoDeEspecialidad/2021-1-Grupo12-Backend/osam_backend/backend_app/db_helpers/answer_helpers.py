from backend_app.db_models.form_tree import FormTree
from backend_app.db_helpers.technician_helpers import get_technician_name_redes, complete_technician
from backend_app.db_helpers.location_helpers import get_location
from backend_app.db_helpers.user_helpers import get_auditor
import datetime


def complete_answer_data(answers_data):
    """Completes all the blank parts in the answer structure."""
    answers_data["metadata"]["category_data"] = complete_category(
        answers_data["metadata"]["category_data"],
        answers_data["category_id"],
        answers_data["audit_type_id"],
        answers_data["service_type_id"])
    answers_data["metadata"]["location_data"] = get_location(
        answers_data["commune_id"],
        answers_data["metadata"]["location_data"]
    )
    answers_data["metadata"]["technician_data"] = complete_technician(
        answers_data["metadata"]["technician_data"],
        answers_data["category_id"],
        answers_data["auditor_id"],
        answers_data["metadata"]["timestamp_data"]["final_timestamp"]
    )
    answers_data["metadata"]["auditor_data"] = get_auditor(
        answers_data["auditor_id"],
        answers_data["metadata"]["auditor_data"]
    )
    answers_data["exit_timestamp"] = set_exit_timestamp(
        answers_data["metadata"]["timestamp_data"]
    )

    answers_data["metadata"]["timestamp_data"] = complete_timestamp(
        answers_data["metadata"]["timestamp_data"]
    )
    return answers_data


def complete_category(category_data, 
                      category_id, 
                      audit_type_id, 
                      service_type_id):
    """Complete the category information into the answer."""

    formtree = FormTree.objects.all().last()
    category = formtree.tree[category_id]
    levels = category["levels"]
    audit_type = category["audit_types"][audit_type_id]
    category_data["category_name"] = category["name"]
    category_data["audit_type"] = audit_type["name"]
    if levels > 1:
        service = audit_type["service_types"][service_type_id]
        category_data["service_type"] = service["name"].upper()
    return category_data


def split_timestamp(timestamp):
    """Splits the timestamp in time and date."""

    raw_init_date, raw_init_time = timestamp.split("T")
    year, month, day = raw_init_date.split("-")
    hr, min, secs = raw_init_time.split(":")
    day = int(day)
    month = int(month)
    hr = int(hr)
    secs = secs[:2].strip(".")
    clean_date = f"{day}/{month}/{year}"
    clean_time = f"{hr}:{min}:{secs}"
    return clean_date, clean_time


def format_timestamp(timestamp):
    """Change the timestamp format."""

    raw_init_date, raw_init_time = timestamp.split("T")
    year, month, day = raw_init_date.split("-")
    hr, min, _ = raw_init_time.split(":")
    year = year
    day = int(day)
    month = int(month)
    hr = int(hr)
    return f"{day}-{month}-{year} {hr}:{min}"


def complete_timestamp(timestamp_data):
    """Completes the timestamp in the asnwer."""

    init_timestamp = timestamp_data["initial_timestamp"]
    final_timestamp = timestamp_data["final_timestamp"]
    initial_clean_date, initial_clean_time = split_timestamp(init_timestamp)
    timestamp_data["initial_date"] = initial_clean_date
    timestamp_data["initial_time"] = initial_clean_time
    timestamp_data["final_timestamp"] = format_timestamp(final_timestamp)
    return timestamp_data


def set_exit_timestamp(timestamp_data):
    """Set the exit timestamp in the answer."""

    return datetime.datetime.strptime(timestamp_data["final_timestamp"].split(".")[0], "%Y-%m-%dT%H:%M:%S")


def get_timestamps(answer_data):
    """Get answer_data time and dates"""

    timestamp_data = answer_data["metadata"]["timestamp_data"]
    final_timestamp = timestamp_data["final_timestamp"]
    initial_timestamp = timestamp_data["initial_timestamp"]
    initial_time = timestamp_data["initial_time"]
    initial_date = timestamp_data["initial_date"]
    return (final_timestamp, initial_timestamp, initial_time, initial_date)


def string_to_datetime(final_timestamp):
    """Converts final_timestamp to datetime"""

    return datetime.datetime.strptime(final_timestamp, "%d/%m/%Y %H:%M:%S")


def string_to_report_datetime(final_timestamp):
    """Converts final_timestamp to datetime compatible with report format"""

    d = datetime.datetime.strptime(final_timestamp, "%d/%m/%Y %H:%M:%S")
    return d.strftime("%d/%m/%y %H:%M")


def complete_technician_name_redes(answer_data):
    """Update answer_data technician name redes"""
    technicians = answer_data["metadata"]["technician_data"]["technicians"]

    tech1_first = technicians["technician_1"]["technician_first_name"]
    tech1_last = technicians["technician_1"]["technician_last_name"]

    tech2_first = technicians["technician_1"]["technician_first_name"]
    tech2_last = technicians["technician_1"]["technician_last_name"]

    name_redes_1 = get_technician_name_redes(tech1_first, tech1_last)
    name_redes_2 = get_technician_name_redes(tech2_first, tech2_last)

    answer_data["metadata"]["technician_data"]["technicians"]["technician_1"]["technician_name_redes"] = name_redes_1
    answer_data["metadata"]["technician_data"]["technicians"]["technician_2"]["technician_name_redes"] = name_redes_2

    return answer_data
