
from backend_app.db_helpers.report_helpers import request_report
from backend_app.db_validators.report_validators import validate_for_api_patch
from backend_app.db_helpers.report_helpers import update_reports_for_api, get_csv, get_timestamps
from backend_app.db_validators.report_validators import validate_automated_report_data, validate_web_report_data, validate_timestamps, validate_format_name
from backend_app.db_validators.form_tree_validators import validate_category_report
from backend_app.db_validators.block_validators import validate_blocks_report, validate_blocks_are_for_report, check_blocks_category
from backend_app.db_serializers.report_serializer import ReportSerializer
from backend_app.db_helpers.question_helpers import get_question_ids
from backend_app.db_helpers.metadata_helpers import get_metadata_ids
from backend_app.db_helpers.json_helpers import get_indexed_json
from backend_app.db_helpers.form_tree_helpers import get_category_name
from backend_app.db_helpers.user_helpers import get_current_user
from backend_app.db_models.metadata import Metadata
from backend_app.db_models.question import Question
from backend_app.db_models.report import Report
from backend_app.db_models.answer import Answers
from backend_app.db_models.client import Client
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpRequest
from backend_app.db_models.user import User


@api_view(['GET', 'POST'])
def report_list(request):
    """Return all the reports structures and add a report structure."""

    if request.method == 'GET':
        reports = Report.objects.all().order_by('-id')
        report_serializer = ReportSerializer(reports, many=True)
        return JsonResponse(get_indexed_json(report_serializer.data), safe=False, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        report_data = JSONParser().parse(request)
        report_serializer = ReportSerializer(data=report_data)
        if report_serializer.is_valid():
            blocks_obj = report_data['blocks']
            if validate_blocks_report(blocks_obj):
                if validate_blocks_are_for_report(blocks_obj["block_ids"]):
                    if validate_category_report(report_data):
                        if validate_format_name(report_data["name_format"]):
                            if check_blocks_category(blocks_obj["block_ids"], report_data["category"]):
                                report = report_serializer.save()
                                update_reports_for_api(report)
                                report.save()
                                return JsonResponse(report_serializer.data, status=status.HTTP_201_CREATED)
                            else:
                                return JsonResponse({"error": "Blocks belong to different categories"}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return JsonResponse({"error": "The technician name format is not valid"}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return JsonResponse({"error": "Not a valid category"})
                else:
                    return JsonResponse({"error": "Some of the blocks are for form"}, status=status.HTTP_400_BAD_REQUEST)
            report_error = {"error": "The blocks id are not valid"}
            return JsonResponse(report_error, status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(report_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def report_detail(request, pk):
    """The GET, PUT and DELETE method for a report."""

    try:
        report = Report.objects.get(pk=pk)
        if request.method == 'GET':
            report_serializer = ReportSerializer(report)
            return JsonResponse(report_serializer.data)

        elif request.method == 'PUT':
            report_data = JSONParser().parse(request)
            blocks_obj = report_data['blocks']
            report_serializer = ReportSerializer(report, data=report_data)
            if report_serializer.is_valid():
                if validate_blocks_report(blocks_obj):
                    if validate_blocks_are_for_report(blocks_obj["block_ids"]):
                        if validate_category_report(report_data):
                            if validate_format_name(report_data["name_format"]):
                                if check_blocks_category(blocks_obj["block_ids"], report_data["category"]):
                                    report = report_serializer.save()
                                    update_reports_for_api(report)
                                    report.save()
                                    return JsonResponse(report_serializer.data, status=status.HTTP_201_CREATED)
                                else:
                                    return JsonResponse({"error": "Blocks belong to different categories"}, status=status.HTTP_400_BAD_REQUEST)
                            else:
                                return JsonResponse({"error": "The technician name format is not valid"}, status=status.HTTP_400_BAD_REQUEST)
                        else:
                            return JsonResponse({"error": "Not a valid category"}, status=status.HTTP_400_BAD_REQUEST)
                    else:
                        return JsonResponse({"error": "Some of the blocks are for form"}, status=status.HTTP_400_BAD_REQUEST)
                report_error = {"error": "The blocks id are not valid"}
                return JsonResponse(report_error, status=status.HTTP_404_NOT_FOUND)
            return JsonResponse(report_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif request.method == 'PATCH':
            report_data = JSONParser().parse(request)
            report_serializer = ReportSerializer(report, partial=True, data=report_data)
            if report_serializer.is_valid(raise_exception=True):
                if validate_for_api_patch(report_data):
                    report = report_serializer.save()
                    update_reports_for_api(report)
                    report.save()
                    return JsonResponse(report_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return JsonResponse({"error": "only 'for_api' key available for report patch."}, status=status.HTTP_400_BAD_REQUEST)

            return JsonResponse(report_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        elif request.method == 'DELETE':
            report.delete()
            return JsonResponse({'message': 'Report was deleted successfully!'}, status=status.HTTP_201_CREATED)

    except Report.DoesNotExist:
        return JsonResponse({'error': 'The report does not exist'})



@api_view(['POST'])
def generate_report(request, pk):
    """Returns the csv asociated to a report."""

    try:
        report = Report.objects.get(pk=pk)
        report_data = JSONParser().parse(request)
        if validate_web_report_data(report_data):
            if validate_timestamps(report_data):
                return request_report(report, report_data)
            else:
                return JsonResponse({'error': 'The timestamp are incorrect. Check format: %Y-%m-%dT%H:%M:%S or verify datetimes'})
        else:
            return JsonResponse({'error': 'The body of the request was not sent correctly. Change the format'})
    except Report.DoesNotExist:
        return JsonResponse({'error': 'The report does not exist'})


@api_view(['POST'])
def generate_report_client_side(request):
    """Return the csv associated to a report for a client."""

    report_data_json = JSONParser().parse(request)
    if validate_automated_report_data(report_data_json):
        if validate_category_report(report_data_json):
            try:
                client = Client.objects.get(category=report_data_json["category"])
                if report_data_json["token"] != client.token:
                    return JsonResponse({'error': 'Wrong token'})
            except Client.DoesNotExist:
                return JsonResponse({'error': 'Wrong category'})
        else:
            return JsonResponse({'error': 'Wrong category'})

        try:
            report = Report.objects.get(for_api=True, category=report_data_json["category"])
            report_data = {
                "client_entry_timestamp": report_data_json["client_entry_timestamp"],
                "client_exit_timestamp": report_data_json["client_exit_timestamp"]
            }
            if validate_web_report_data(report_data): 
                if validate_timestamps(report_data):
                    return request_report(report, report_data)
                else:
                    return JsonResponse({'error': 'The timestamp are incorrect. Check format: %Y-%m-%dT%H:%M:%S or verify datetimes'})
            else:
                return JsonResponse({'error': 'The body of the request was not sent correctly. Change the format'})

        except Report.DoesNotExist:
            report_name = get_category_name(report_data_json["category"])
            report_data = {
                "question_based": True,
                "name": f"Reporte{report_name}",
                "client_entry_timestamp": report_data_json["client_entry_timestamp"],
                "client_exit_timestamp": report_data_json["client_exit_timestamp"],
                "category": report_data_json["category"],
                "token": report_data_json["token"]
            }

        try:
            if validate_timestamps(report_data):
                if validate_category_report(report_data):
                    (entry_ts, exit_ts) = get_timestamps(report_data)
                    question_ids = [question.id for question in Question.objects.filter(category_id=int(report_data["category"], status=True))]
                    category = "1" if report_data["category"] == "1" else "0"
                    metadata_ids = [metadata.id for metadata in Metadata.objects.all() if category in metadata.category["category_ids"]]
                    answers = Answers.objects.filter(exit_timestamp__gte=entry_ts,
                                         exit_timestamp__lte=exit_ts, category_id=report_data["category"]).order_by('exit_timestamp')
                    return get_csv(metadata_ids, question_ids, answers, 
                            report_data["category"], report_data, is_automated=True)
                else:
                    return JsonResponse({'error': 'The category is wrong'})
            else:
                return JsonResponse({'error': 'The timestamp are incorrect. Check format: %Y-%m-%dT%H:%M:%S or verify datetimes'})

        except Report.DoesNotExist:
            return JsonResponse({'error': 'The report does not exist'})
    else:
        return JsonResponse({'error': 'Key errors in sent request'})

@api_view(['GET'])
def report_for_api(_):
    reports = Report.objects.filter(for_api=True).order_by('-id')
    report_serializer = ReportSerializer(reports, many=True)
    return JsonResponse(get_indexed_json(report_serializer.data), status=status.HTTP_200_OK)

@api_view(['GET'])
def reports_for_user_category(request):
    """GetAll reports for the corresponding category for a user."""

    user = get_current_user(request)
    if user._type == 1:
        reports = Report.objects.all()
    elif user._type == 2:
        reports = Report.objects.filter(only_admin=False).order_by('-id')
    else:
        category = user.category_id
        reports = Report.objects.filter(category=category, only_admin=False).order_by('-id')

    report_serializer = ReportSerializer(reports, many=True)
    return JsonResponse(get_indexed_json(report_serializer.data), safe=False, status=status.HTTP_200_OK)

@api_view(['GET'])
def reports_by_category(_, category):
    """GetAll reports for a category. Only for admin."""
    reports = Report.objects.filter(category=category).order_by('-id')
    report_serializer = ReportSerializer(reports, many=True)
    return JsonResponse(get_indexed_json(report_serializer.data), safe=False, status=status.HTTP_200_OK)
    