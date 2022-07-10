import datetime
from backend_app.db_helpers.report_keys import FORMAT_OPTIONS


def validate_timestamps(json_data):
    """Validate the timestamp format."""

    if "client_entry_timestamp" in json_data and "client_exit_timestamp" in json_data:
        entry_ts = json_data["client_entry_timestamp"]
        exit_ts = json_data["client_exit_timestamp"]
        # Delete milliseconds:"2021-01-25T22:32:33.123000" -> "2021-01-25T22:32:33"
        entry_ts = entry_ts.split(".")[0]
        exit_ts = exit_ts.split(".")[0]
        try:
            # Validate datetime format
            # Correct format example: "2021-01-25T22:32:33"
            entry_datetime = datetime.datetime.strptime(entry_ts, "%Y-%m-%dT%H:%M:%S")
            exit_datetime = datetime.datetime.strptime(exit_ts, "%Y-%m-%dT%H:%M:%S")

            # Entry has to be before exit
            if entry_datetime >= exit_datetime:
                return False

            # # Entry cannot be in the future
            if entry_datetime > datetime.datetime.now():
                return False
        except ValueError:
            return False

        return True
    return False

def validate_automated_report_data(json_data):
    """Validate the data of the body of the automated report."""

    if len(json_data.keys()) == 4:
        if ("client_entry_timestamp" in json_data and "client_exit_timestamp" in json_data and "category" in json_data and "token" in json_data):
            return True
    return False

def validate_web_report_data(json_data):
    """Validate request for report generation."""

    if len(json_data.keys()) == 2:
        if ("client_entry_timestamp" in json_data and "client_exit_timestamp" in json_data):
            return True
    return False

def validate_format_name(format_name):
    """Validate that the format name is one among the choices."""

    if format_name not in FORMAT_OPTIONS:
        return False
    return True

def validate_for_api_patch(json_data):
    if len(json_data.keys()) == 1:
        if "for_api" in json_data.keys():
            return True
    return False
        