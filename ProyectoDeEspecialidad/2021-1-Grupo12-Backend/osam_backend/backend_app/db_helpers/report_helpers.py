from backend_app.db_models.metadata import Metadata
from backend_app.db_models.answer import Answers
from backend_app.db_helpers.metadata_helpers import get_metadata_header
from backend_app.db_helpers.question_helpers import get_values_header, get_values_header_auto
from backend_app.db_helpers.technician_helpers import get_name_redes
from backend_app.db_helpers.question_helpers import get_question_ids
from backend_app.db_helpers.metadata_helpers import get_metadata_ids
from backend_app.db_models.report import Report
from django.http import HttpResponse
import csv
import codecs


def get_csv(metadata_ids, question_ids, answers, category, report, is_enumerated=False, is_automated=False):
    """Returns the csv for the report."""

    response = HttpResponse(content_type='text/csv')
    if is_automated:
        csv_name = report["name"]
        csv_header = get_metadata_header(metadata_ids) + get_values_header_auto(question_ids)
        format = "inverted_camel_case_comma" if category == "1" else "all_caps"
    else:
        csv_name = report.name
        csv_header = get_metadata_header(metadata_ids) + get_values_header(question_ids, is_enumerated, report)
        format = report.name_format
    response['Content-Disposition'] = f'attachment; filename="{csv_name}.csv"'
    response.write(codecs.BOM_UTF8)
    writer = csv.writer(response)
    writer.writerow(csv_header)
    metadata_list = [Metadata.objects.get(id=metadata_id) 
                     for metadata_id in metadata_ids]

    for answer in answers:
        answer_metadata = answer.metadata
        row = []
        for metadata in metadata_list:
            try:
                metadata_copy = answer_metadata.copy()
                for route in metadata.route:
                    metadata_copy = metadata_copy[route]
                if metadata.name == "Nombre Tecnico" or metadata.name == "Nombre Tecnico 1":
                    first_technician_data = answer_metadata["technician_data"]["technicians"]["technician_1"]
                    metadata_copy = name_formatter(first_technician_data["technician_first_name"], first_technician_data["technician_last_name"], format)
                if metadata.name == "Nombre Tecnico 2":
                    second_technician_data = answer_metadata["technician_data"]["technicians"]["technician_2"]
                    metadata_copy = name_formatter(second_technician_data["technician_first_name"], second_technician_data["technician_last_name"], format)
            except (TypeError, KeyError):
                metadata_copy = "ERROR"
            row.append(metadata_copy)
        for question_id in question_ids:
            if str(question_id) in answer.values:
                row.append(answer.values[str(question_id)])
            else:
                row.append(None)

        writer.writerow(row)
    return response


def get_timestamps(timestamps_data):
    """Returns the timestamps."""

    return (timestamps_data["client_entry_timestamp"].split(".")[0], 
            timestamps_data["client_exit_timestamp"].split(".")[0])


def update_reports_for_api(report):
    if report.for_api:
        reports_for_api = Report.objects.filter(for_api=True, category=report.category)
        for report_for_api in reports_for_api:
            report_for_api.for_api = False
            report_for_api.save()


def check_report_dependencies(block):
    """Checks if block belongs to any form."""

    allowed_to_delete = True
    report_dependency_list = []
    reports = Report.objects.filter(category=block.category)
    for report in reports:
        if block.id in report.blocks["block_ids"]:
            allowed_to_delete = False
            report_dependency_list.append({"id": report.id, "name": report.name})
    return (report_dependency_list, allowed_to_delete)

def name_formatter(first_name_string, last_name_string, format):
    """Gets first names and last names from answers and a format type, and it applies
        that format to return the full name."""
        
    full_name = ""
    if first_name_string != "":
        if format == "inverted_camel_case_comma":
            if " " in last_name_string:
                last_names_list = [name.capitalize() for name in last_name_string.split(" ")]
                last_names = " ".join(last_names_list)
            else:
                last_names = last_name_string.capitalize()
            if " " in first_name_string:
                first_names_list = [name.capitalize() for name in first_name_string.split(" ")]
                first_names = " ".join(first_names_list)
            else:
                first_names = first_name_string.capitalize()
            full_name = f"{last_names}" + ", " + f"{first_names}"
        elif format == "camel_case_comma":
            if " " in last_name_string:
                last_names_list = [name.capitalize() for name in last_name_string.split(" ")]
                last_names = " ".join(last_names_list)
            else:
                last_names = last_name_string.capitalize()
            if " " in first_name_string:
                first_names_list = [name.capitalize() for name in first_name_string.split(" ")]
                first_names = " ".join(first_names_list)
            else:
                first_names = first_name_string.capitalize()
            full_name = f"{first_names}" + ", " + f"{last_names}"
        elif format == "all_caps":
            full_name = first_name_string.upper() + " " + last_name_string.upper()
        elif format == "inverted_all_caps":
            full_name = last_name_string.upper() + " " + first_name_string.upper()
        elif format == "all_minus":
            full_name = first_name_string.lower() + " " + last_name_string.lower()
        elif format == "inverted_all_minus":
            full_name = last_name_string.lower() + " " + first_name_string.lower()
        elif format == "camel_case":
            full_name = first_name_string + " " + last_name_string
        elif format == "inverted_camel_case":
            full_name = last_name_string + " " + first_name_string
    return full_name

def request_report(report, report_data):
    """Gets answers and returns csv."""

    (entry_ts, exit_ts) = get_timestamps(report_data)
    question_ids = get_question_ids(report)
    metadata_ids = get_metadata_ids(report)
    answers = Answers.objects.filter(exit_timestamp__gte=entry_ts,
                            exit_timestamp__lte=exit_ts, category_id=report.category).order_by('exit_timestamp')
    return get_csv(metadata_ids, question_ids, answers, report.category, 
                report, is_enumerated=report.is_enumerated)